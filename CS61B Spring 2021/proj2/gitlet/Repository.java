package gitlet;

import java.io.File;
import static gitlet.Utils.*;


/** Represents a gitlet repository.
 * .gitlet/  (repository directory).
 * .gitlet/objects/  (metadata for commits and the blobs objects)
 * .gitlet/HEAD  (current HEAD)
 * .gitlet/index  (staging area)
 * .gitlet/refs/heads/  (branch head)
 *  @author hdx
 */
public class Repository {
    /** The current working directory as File.*/
    public static final File CWD = new File(System.getProperty("user.dir"));
    /** The .gitlet directory as File (DIR). */
    public static final File GITLET_DIR = join(CWD, ".gitlet");
    /** The staging area. */
    private static StagingArea STAGING_AREA = new StagingArea();
    /** The current HEAD. */
    private static final File HEAD_DIR = join(CWD, ".gitlet/HEAD");
    /** The branch HEAD. */
    private static final File BRANCH_HEAD_DIR = join(CWD, ".gitlet/refs/heads");

    public static void init() {
        if (GITLET_DIR.exists()) {
            System.out.println("A Gitlet version-control system already exists in the current directory.");
            return;
        } else {
            GITLET_DIR.mkdir();
        }
        // Get the current working directory
        Commit initial = new Commit("initial commit", null, null);
        Utils.writeObject(HEAD_DIR, initial.getUID());
        initial.dump();
    }

    /**
     * Adds a copy of the file as it currently exists to the staging area
     */
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

    /**
     * Creates a new commit, saves tracked files in the current commit and staging Area.
     */
    public static void commit(String message) {
        if (message.equals("")) {
            System.out.println("Please enter a commit message.");
            return;
        }

        if (STAGING_AREA.getStagedBlobs().isEmpty()) {
            System.out.println("No changes added to the commit.");
            return;
        }

        // dumps files in the staging area to the current commit.
        for (Blob blob : STAGING_AREA.getStagedBlobs()) {
            blob.dump();
        }

        // creates a new commit and dumps it.
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit commit = Commit.fromUID(HEAD);
        commit.update(STAGING_AREA.getStagedBlobs(), message);
        Utils.writeObject(HEAD_DIR, commit.getUID());  //update the HEAD
        STAGING_AREA = new StagingArea();  // clears the staging area.
        STAGING_AREA.dump();
    }

    /** Removes the file: Unstage the file if it is currently staged for addition. If the file is tracked
     * in the current commit, stage it for removal and remove the file from the working directory if the
     * user has not already done so (do not remove it unless it is tracked in the current commit). */
    public static void rm(String filename) {
        Blob blob = new Blob(new File(filename));
        // If the file is currently staged for addition, unstage it.
        if (STAGING_AREA.getStagedBlobs().contains(blob)) {
            STAGING_AREA.removeFromStagingArea(blob);
            STAGING_AREA.dump();
            return;
        }

        // If the file is tracked in the current commit, stage it for removal.
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit commit = Commit.fromUID(HEAD);
        if (commit.getTrackedBlobs().containsKey(filename)) {
            STAGING_AREA.removeBlob(blob);
            STAGING_AREA.dump();
            // remove the file from the working directory if the user has not already done so.
            restrictedDelete(filename);
            return;
        }

        // If the file is not tracked in the current commit, print an error message.
        System.out.println("No reason to remove the file.");
    }

    /**  Starting at the current head commit, display information about each commit
     * backwards along the commit tree until the initial commit, following the first parent commit links,
     * ignoring any second parents found in merge commits. For every node in this history, the information
     * it should display is the commit id, the time the commit was made, and the commit message.*/
    public static void log() {
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit commit = Commit.fromUID(HEAD);
        while (commit != null) {
            System.out.println("===");
            System.out.println("commit " + commit.getUID());
            System.out.println("Date: " + commit.getTimestamp());
            System.out.println(commit.getMessage());
            System.out.println();
            commit = Commit.fromUID(commit.getParent());
        }
    }
}