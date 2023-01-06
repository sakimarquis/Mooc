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
        // check if the Blob has the same filename as the blob in the last commit
        if (lastCommit == null || lastCommit.getTrackedBlobs().containsKey(blob.getUID())) {
            // if not the same, add the file to the staging area
            STAGING_AREA.addBlob(blob);
            STAGING_AREA.dump();
        } else {
            // if that same Blob is already in the staging area, remove it
            if (STAGING_AREA.getStagedBlobs().contains(blob)) {
                STAGING_AREA.removeFromStagingArea(blob);
                STAGING_AREA.dump();
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
        Commit commit = new Commit(message, STAGING_AREA.getAdditionUID(), HEAD);
        commit.dump();
        Utils.writeObject(HEAD_DIR, commit.getUID());

        // clears the staging area.
        STAGING_AREA = new StagingArea();
    }
}
