package gitlet;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.List;
import java.util.HashMap;

import static gitlet.Utils.*;

/** Represents a gitlet repository.
 * .gitlet/  (repository directory).
 * .gitlet/objects/  (metadata for commits and the blobs objects)
 * .gitlet/HEAD  (current HEAD)
 * .gitlet/index  (staging area)
 * .gitlet/refs/heads/  (branch pointers including the master branch)
 *  @author hdx
 */
public class Repository {
    /** The current working directory as File.*/
    public static final File CWD = new File(System.getProperty("user.dir"));
    /** The .gitlet directory as File (DIR). */
    public static final File GITLET_DIR = join(CWD, ".gitlet");
    /** The current HEAD. */
    public static final File HEAD_DIR = join(CWD, ".gitlet/HEAD");
    /** The branch directory. */
    public static final File BRANCH_DIR = join(CWD, ".gitlet/refs/heads");
    public static final File OBJECT_DIR = join(CWD, ".gitlet/objects");

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
        Branch master = new Branch("master", initial.getUID());
        initial.dump();
        master.dump();
        StagingArea.clear();
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
        // get the staging area
        StagingArea STAGING_AREA = StagingArea.load();
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

        StagingArea STAGING_AREA = StagingArea.load();

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
        StagingArea.clear();
    }

    /** Removes the file: Unstage the file if it is currently staged for addition. If the file is tracked
     * in the current commit, stage it for removal and remove the file from the working directory if the
     * user has not already done so (do not remove it unless it is tracked in the current commit). */
    public static void rm(String filename) {
        Blob blob = new Blob(new File(filename));
        StagingArea STAGING_AREA = StagingArea.load();
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
        String parent = readObject(HEAD_DIR, String.class);
        while (parent != null) {
            Commit commit = Commit.fromUID(parent);
            commit.printLog();
            parent = commit.getParent();
        }
    }

    /**  Display information about all commits ever made. */
    public static void globalLog() {
        try {
            List<Path> filePaths = getFilesRecursively(OBJECT_DIR);
            for (Path filePath : filePaths) {
                Dumpable dumpObj = Utils.readObject(filePath.toFile(), Dumpable.class);
                if (dumpObj instanceof Commit) {
                    Commit commit = (Commit) dumpObj;
                    commit.printLog();
                }
            }
        } catch (IOException e) {
            throw error("IOException");
        }
    }

    /** Prints out the ids of all commits that have the given commit message, one per line. */
    public static void find(String message) {
        boolean found = false;
        try {
            List<Path> filePaths = getFilesRecursively(OBJECT_DIR);
            for (Path filePath : filePaths) {
                Dumpable dumpObj = Utils.readObject(filePath.toFile(), Dumpable.class);
                if (dumpObj instanceof Commit) {
                    Commit commit = (Commit) dumpObj;
                    if (commit.getMessage().contains(message)) {
                        System.out.println(commit.getUID());
                        found = true;
                    }
                }
            }
            if (!found) {
                System.out.println("Found no commit with that message.");
            }
        } catch (IOException e) {
            throw error("IOException");
        }
    }

    /** Displays what branches currently exist, and marks the current branch with a *.
     * Also displays what files have been staged for addition or removal. */
     public static void status() {
        // print out all the branches
        System.out.println("=== Branches ===");
        List<String> branches = Utils.plainFilenamesIn(BRANCH_DIR);
        for (String branch : branches) {
            if (Branch.getCommitUID(branch).equals(readObject(HEAD_DIR, String.class))) {
                System.out.println("*" + branch);
            } else {
                System.out.println(branch);
            }
        }

        // print out all the files that have been staged for addition
        System.out.println();
        System.out.println("=== Staged Files ===");
        StagingArea STAGING_AREA = StagingArea.load();
        for (Blob blob : STAGING_AREA.getStagedBlobs()) {
            System.out.println(blob.getFilename());
        }

        // print out all the files that have been staged for removal
        System.out.println();
        System.out.println("=== Removed Files ===");
        for (Blob blob : STAGING_AREA.getRemovalBlob()) {
            System.out.println(blob.getFilename());
        }

        // print out all the files that have been modified but not staged for commit
        System.out.println();
        System.out.println("=== Modifications Not Staged For Commit ===");

        // print out all the files that are untracked
        System.out.println();
        System.out.println("=== Untracked Files ===");
     }

    /** checkout -- [file name]:
     * Takes the version of the file as it exists in the head commit and puts it in the working directory, overwriting
     * the version of the file that’s already there if there is one. The new version of the file is not staged. */
    public static void checkoutFile(String filename) {
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit commit = Commit.fromUID(HEAD);
        if (!commit.getTrackedBlobs().containsKey(filename)) {
            System.out.println("File does not exist in that commit.");
            return;
        }
        Blob blob = Blob.fromUID(commit.getTrackedBlobs().get(filename));
        blob.writeToFile(filename);
        //
    }

    /** checkout [commit id] -- [file name]:
     * Takes the version of the file as it exists in the commit with the given id, and puts it in the working directory,
     * overwriting the version of the file that’s already there if there is one. The new version of the file is not
     * staged. */
    public static void checkoutFileInCommit(String commitID, String filename) {
        Commit.checkExists(commitID);

        Commit commit = Commit.fromUID(commitID);

        if (!commit.getTrackedBlobs().containsKey(filename)) {
            System.out.println("File does not exist in that commit.");
            return;
        }

        Blob blob = Blob.fromUID(commit.getTrackedBlobs().get(filename));
        blob.writeToFile(filename);
    }

    /** checkout [branch name]:
     * Takes all files in the commit at the head of the given branch, and puts them in the working directory,
     * overwriting the versions of the files that are already there if they exist. Also, at the end of this command,
     * the given branch will now be considered the current branch (HEAD). Any files that are tracked in the current
     * branch but are not present in the checked-out branch are deleted. The staging area is cleared, unless the
     * checked-out branch is the current branch. */
    public static void checkoutBranch(String branchName) {
        Branch.checkExists(branchName);
        Branch.checkCurrentBranch(branchName);

        deleteTrackedFiles();  // delete files that are tracked in the current branch

        // copy files from the checked-out branch
        String commitUID = Branch.getCommitUID(branchName);
        checkoutFilesInCommit(commitUID);

        // update the current HEAD pointer
        writeObject(HEAD_DIR, commitUID);

        StagingArea.clear();
    }

    /** Creates a new branch with the given name, and points it at the current head commit. */
    public static void branch(String branchName) {
        String HEAD = readObject(HEAD_DIR, String.class);
        Branch branch = new Branch(branchName, HEAD);
        branch.dump();
    }

    /** Deletes the branch with the given name. This only means to delete the pointer associated with the branch;
     * it does not mean to delete all commits that were created under the branch, or anything like that. */
    public static void rmBranch(String branchName) {
        if (Branch.getCommitUID(branchName).equals(readObject(HEAD_DIR, String.class))) {
            System.out.println("Cannot remove the current branch.");
            return;
        }
        Branch.delete(branchName);
    }

    /** Checks out all the files tracked by the given commit. Removes tracked files that are not present in that commit.
     *  Also moves the current branch’s head to that commit node. The staging area is cleared.
     *  The command is essentially checkout of an arbitrary commit that also changes the current branch head. */
    public static void reset(String commitUID) {
        Commit.checkExists(commitUID);

        deleteTrackedFiles();  // delete files that are tracked in the current branch

        // copy files from the checked-out branch
        checkoutFilesInCommit(commitUID);

        // update the current HEAD pointer
        writeObject(HEAD_DIR, commitUID);

        StagingArea.clear();
    }


    /** Below are helper functions. */

    /** Delete files that are tracked in the current branch */
    public static void deleteTrackedFiles() {
        String HEAD = readObject(HEAD_DIR, String.class);
        Commit currentCommit = Commit.fromUID(HEAD);
        HashMap<String, String> currentTrackedBlobs = currentCommit.getTrackedBlobs();
        for (String filename : currentTrackedBlobs.keySet()) {
            if (!currentTrackedBlobs.containsKey(filename)) {
                restrictedDelete(filename);
            }
        }
    }

    /** copy files from the checked-out commit. */
    public static void checkoutFilesInCommit(String commitUID) {
        Commit commit = Commit.fromUID(commitUID);
        HashMap<String, String> trackedBlobs = commit.getTrackedBlobs();
        for (String filename : trackedBlobs.keySet()) {
            Blob blob = Blob.fromUID(trackedBlobs.get(filename));
            // If a working file is untracked in the current branch and would be overwritten by the checkout
            File file = new File(filename);
            if (file.exists()) {
                System.out.println("There is an untracked file in the way; delete it, or add and commit it first.");
                return;
            }
            blob.writeToFile(filename);
        }
    }
}