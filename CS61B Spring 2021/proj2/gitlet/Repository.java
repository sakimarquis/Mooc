package gitlet;

import java.io.File;
import static gitlet.Utils.*;


/** Represents a gitlet repository.
 *  @author hdx
 */
public class Repository {
    /**
     * TODO: add instance variables here.
     *
     * List all instance variables of the Repository class here with a useful
     * comment above them describing what that variable represents and how that
     * variable is used. We've provided two examples for you.
     */

    /** The current working directory as File. */
    public static final File CWD = new File(System.getProperty("user.dir"));
    /** The .gitlet directory as File (DIR). */
    public static final File GITLET_DIR = join(CWD, ".gitlet");
    /** The staging area. */
    private static StagingArea STAGING_AREA = new StagingArea();
    /** The current HEAD. */
    private static final File HEAD_DIR = join(CWD, ".gitlet/HEAD");

    public static void init() {
        if (GITLET_DIR.exists()) {
            System.out.println("A Gitlet version-control system already exists in the current directory.");
            return;
        } else {
            GITLET_DIR.mkdir();
        }
        // Get the current working directory
        Commit initial = new Commit("initial commit", null, null);
        System.out.println(HEAD_DIR);
        Utils.writeObject(HEAD_DIR, initial.getUID());
        initial.dump();
    }

    /** Adds a copy of the file as it currently exists to the staging area */
    public static void add(String filename) {
        File file = new File(filename);
        if (!file.exists()) {
            System.out.println("File does not exist.");
            return;
        }
        Blob blob = new Blob(file);
        // read the current HEAD
        String HEAD = readObject(HEAD_DIR, String.class);
        // get the last commit
        Commit lastCommit = Commit.fromUID(HEAD);
        // If the Blob has the different filename with all the blobs in the last commit
        if (!lastCommit.getTrackedBlobs().containsKey(filename)) {
            // add the blob to the staging area
            STAGING_AREA.addBlob(blob);
            STAGING_AREA.dump();
        } else {
            // If the Blob has the different content (UID) with the blob in the last commit
            if (!lastCommit.getTrackedBlobs().containsValue(blob.getUID())) {
                STAGING_AREA.addBlob(blob);
                STAGING_AREA.dump();
            } else {
                // if the Blob has the different content (UID), and it is already in the staging area
                if (STAGING_AREA.getStagedBlobs().contains(blob)) {
                    STAGING_AREA.removeFromStagingArea(blob);
                    STAGING_AREA.dump();
                }
            }
        }
    }

    /** Creates a new commit, saves tracked files in the current commit and staging Area. */
    public static void commit(String message) {
        if (message.equals("")) {
            System.out.println("Please enter a commit message.");
            return;
        }

        // dumps files in the staging area to the current commit.
        for (Blob blob : STAGING_AREA.getStagedBlobs()) {
            blob.dump();
        }

        // creates a new commit and dumps it.
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit commit = Commit.fromUID(HEAD);
        commit.addBlobs(STAGING_AREA.getStagedBlobs());
        commit.dump();
        Utils.writeObject(HEAD_DIR, commit.getUID());

        // clears the staging area.
        STAGING_AREA = new StagingArea();
    }
}
