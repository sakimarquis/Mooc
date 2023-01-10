package gitlet;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.HashMap;

import static gitlet.Utils.*;

/** Represents a gitlet repository.
 * .gitlet/  (repository directory).
 * .gitlet/objects/  (metadata for commits and the blobs objects)
 * .gitlet/HEAD  (current HEAD branch, only stores the name of the branch, default is master)
 * .gitlet/index  (staging area)
 * .gitlet/refs/heads/  (branch (pointers) including the master branch)
 *  @author hdx
 */
public class Repository {
    /** The current working directory as File.*/
    public static final File CWD = new File(System.getProperty("user.dir"));
    /** The .gitlet directory as File (DIR). */
    public static final File GITLET_DIR = join(CWD, ".gitlet");
    /** The current HEAD. */
    public static final File HEAD_FILE = join(CWD, ".gitlet/HEAD");
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
        Branch master = new Branch("master", initial.getUID());
        initial.dump();
        Utils.writeObject(HEAD_FILE, "master");
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
        // get the HEAD commit
        Commit lastCommit = Commit.fromUID(Branch.getHeadCommitUID());
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
        Commit commit = Commit.fromUID(Branch.getHeadCommitUID());
        commit.update(STAGING_AREA.getStagedBlobs(), message);
        Branch.updateHEAD(commit.getUID());  //update the commitUID that HEAD branch points
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
        Commit commit = Commit.fromUID(Branch.getHeadCommitUID());
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
        String parent = Branch.getHeadCommitUID();
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
            if (branch.equals(readObject(HEAD_FILE, String.class))) {
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
        for (String filename : getModifiedFiles()) {
            System.out.println(filename);
        }

        // print out all the files that are untracked
        System.out.println();
        System.out.println("=== Untracked Files ===");
        for (String filename : getUntrackedFiles()) {
            System.out.println(filename);
        }
     }

    /** checkout -- [file name]:
     * Takes the version of the file as it exists in the head commit and puts it in the working directory, overwriting
     * the version of the file that’s already there if there is one. The new version of the file is not staged. */
    public static void checkoutFile(String filename) {
        Commit commit = Commit.fromUID(Branch.getHeadCommitUID());
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
        if (Branch.isBranchHEAD(branchName)) {
            System.out.println("No need to checkout the current branch.");
            return;
        }

        // delete files that are tracked in the current branch
        deleteTrackedFiles();
        // copy files from the checked-out branch
        String commitUID = Branch.getCommitUID(branchName);
        checkoutFilesInCommit(commitUID);

        // update HEAD, first change HEAD than update the commitUID that HEAD branch points
        Branch.changeHEAD(branchName);
        Branch.updateHEAD(commitUID);

        StagingArea.clear();
    }

    /** Creates a new branch with the given name, and points it at the current head commit. */
    public static void branch(String branchName) {
        Branch branch = new Branch(branchName, Branch.getHeadCommitUID());
        branch.dump();
    }

    /** Deletes the branch with the given name. This only means to delete the pointer associated with the branch;
     * it does not mean to delete all commits that were created under the branch, or anything like that. */
    public static void rmBranch(String branchName) {
        if (Branch.isBranchHEAD(branchName)) {
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
        checkoutFilesInCommit(commitUID);  // copy files from the checked-out branch

        // update the current HEAD pointer
        Branch.updateHEAD(commitUID);

        StagingArea.clear();
    }

    /** Merges files from the given branch into the current branch.
     * 1, Files in Split point, files modified in the other but not modified in the HEAD branch: -> other branch, stage
     * 2, Files in Split point, files modified in the HEAD but not modified in the other branch: -> HEAD branch
     * 3, Files in Split point, files modified in both branches
     * 3.1, in the same way: nothing to do
     * 3.2, in the different ways: CONFLICT
     * 4, Files in Split point, files removed in the other but not removed in the HEAD branch: -> remove, stage
     * 5, Files in Split point, files removed in the HEAD but not modified in the other branch: -> remove
     * 6, Files not in Split point nor the other branch, but in the HEAD branch: -> HEAD branch
     * 7, Files not in Split point nor the HEAD branch, but in the other branch: -> other branch, stage
     * "I must confess that I wrote Fortran in Java."
     * */
    public static void merge(String branchName) {
        Branch.checkExists(branchName);

        String givenCommitUID = Branch.getCommitUID(branchName);

        // If attempting to merge a branch with itself
        if (Branch.isBranchHEAD(branchName)) {
            Utils.exitWithError("Cannot merge a branch with itself.");
        }

        // If there are staged additions or removals present
        if (!StagingArea.isEmpty()) {
            Utils.exitWithError("You have uncommitted changes.");
        }

        String splitCommitUID = Branch.findSplitPoint(branchName);
        assert splitCommitUID != null;

        // If the split point is the same commit as the given branch, then we do nothing; the merge is complete
        if (givenCommitUID.equals(splitCommitUID)) {
            Utils.exitWithError("Given branch is an ancestor of the current branch.");
        }

        // If the split point is the current branch, then the effect is to check out the given branch
        // In other words, if the current branch has no new commits and the other branch has new commits,
        // simply "fast-forward" the current branch to the other branch
        if (splitCommitUID.equals(Branch.getHeadCommitUID())) {
            checkoutBranch(branchName);
            System.out.println("Current branch fast-forwarded.");
            return;
        }

        Commit currentCommit = Commit.fromUID(Branch.getHeadCommitUID());
        Commit givenCommit = Commit.fromUID(givenCommitUID);
        Commit splitCommit = Commit.fromUID(splitCommitUID);
        HashMap<String, String> currentTrackedBlobs = currentCommit.getTrackedBlobs();
        HashMap<String, String> givenTrackedBlobs = givenCommit.getTrackedBlobs();
        HashMap<String, String> splitTrackedBlobs = splitCommit.getTrackedBlobs();

        // Current branch and the given branch are equal, no commit should be made
        if (currentTrackedBlobs.equals(givenTrackedBlobs)) {
            Utils.exitWithError("No changes added to the commit.");
        }

        HashMap<String, String> mergedTrackedBlobs = new HashMap<>();
        StagingArea STAGING_AREA = StagingArea.load();

        // For files in the split point commit
        for (String key : splitTrackedBlobs.keySet()) {
            boolean currentHasFile = currentTrackedBlobs.containsKey(key);
            boolean givenHasFile = givenTrackedBlobs.containsKey(key);
            String fileUIDInSplit = splitTrackedBlobs.get(key);
            String fileUIDInGiven = givenTrackedBlobs.get(key);
            String fileUIDInCurrent = currentTrackedBlobs.get(key);

            // 3.1, in the same way (a file was removed from both the current and given branch)
            if (!currentHasFile && !givenHasFile) {
                break;
            }
            else if (currentHasFile && givenHasFile) {
                // 1, files modified in the given but not modified in the HEAD branch: -> other branch, stage
                if (!fileUIDInSplit.equals(fileUIDInGiven) && fileUIDInSplit.equals(fileUIDInCurrent)) {
                    String blobUID = givenTrackedBlobs.get(key);
                    STAGING_AREA.addBlob(Blob.fromUID(blobUID));
                }
                // 2, files modified in the HEAD but not modified in the other branch: -> HEAD branch
                else if (fileUIDInSplit.equals(fileUIDInGiven) && !fileUIDInSplit.equals(fileUIDInCurrent)) {
                    mergedTrackedBlobs.put(key, currentTrackedBlobs.get(key));
                }
                // 3.1, files modified in the same way: nothing to do
                else if (fileUIDInCurrent.equals(fileUIDInGiven)) {
                    break;
                }
                // 3.2, files in split point and modified in the different ways: CONFLICT
                else if (!fileUIDInCurrent.equals(fileUIDInGiven)) {
                    String mergedBlobUID = Blob.merge(givenTrackedBlobs.get(key), currentTrackedBlobs.get(key));
                    mergedTrackedBlobs.put(key, mergedBlobUID);
                }
            } else if (currentHasFile && !givenHasFile) {
                // 4, files removed in the other but stay the same the HEAD branch: -> remove, stage
                if (fileUIDInSplit.equals(currentHasFile)) {
                    STAGING_AREA.removeBlob(currentTrackedBlobs.get(key));
                }
                // 3.2, files removed in the other but changed in the HEAD branch: CONFLICT
                else {
                    String blobUID = givenTrackedBlobs.get(key);
                    mergedTrackedBlobs.put(key, blobUID);
                }
            } else if (currentHasFile && !givenHasFile) {
                // 5, files removed in the HEAD but not modified in the other branch: -> remove (nothing to do)
                if (fileUIDInSplit.equals(fileUIDInCurrent)) {
                    break;
                }
                // 3.2, files removed in the HEAD but changed in the other branch: CONFLICT
                else {
                    String blobUID = givenTrackedBlobs.get(key);
                    mergedTrackedBlobs.put(key, blobUID);
                }
            }
        }

        // 6, Files not in Split point nor the other branch, but in the HEAD branch: -> HEAD branch
        HashSet<String> currentUniqueFiles = new HashSet<>(currentTrackedBlobs.keySet());
        currentUniqueFiles.removeAll(splitTrackedBlobs.keySet());
        currentUniqueFiles.removeAll(givenTrackedBlobs.keySet());

        if (!currentUniqueFiles.isEmpty()) {
            for (String key : currentUniqueFiles) {
                String blobUID = currentTrackedBlobs.get(key);
                mergedTrackedBlobs.put(key, blobUID);
            }
        }

        // 7, Files not in Split point nor the HEAD branch, but in the other branch: -> other branch, stage
        HashSet<String> givenUniqueFiles = new HashSet<>(givenTrackedBlobs.keySet());
        givenUniqueFiles.removeAll(splitTrackedBlobs.keySet());
        givenUniqueFiles.removeAll(currentTrackedBlobs.keySet());

        if (!givenUniqueFiles.isEmpty()) {
            for (String key : givenUniqueFiles) {
                String blobUID = givenTrackedBlobs.get(key);
                STAGING_AREA.addBlob(Blob.fromUID(blobUID));
            }
        }

        // 3.2, Files not in Split point, but different in the HEAD and given branch : CONFLICT
        HashSet<String> conflictFiles = new HashSet<>(currentTrackedBlobs.keySet());
        conflictFiles.retainAll(givenTrackedBlobs.keySet());
        conflictFiles.removeAll(splitTrackedBlobs.keySet());

        if (!conflictFiles.isEmpty()) {
            for (String key : conflictFiles) {
                String blobUID = givenTrackedBlobs.get(key);
                mergedTrackedBlobs.put(key, blobUID);
            }
        }

        // Finally, make the commit and dump it, change the HEAD and dump it
        String msg = "Merged " + branchName + " into " + Branch.getBranchNameFromUID(Branch.getHeadCommitUID()) + ".";
        Commit mergedCommit = new Commit(msg, mergedTrackedBlobs, givenCommitUID, Branch.getHeadCommitUID());
        mergedCommit.dump();
        STAGING_AREA.dump();
        checkoutFilesInCommit(mergedCommit.getUID());  // update CWD
        Branch.changeHEAD(branchName);  // update the HEAD
        Branch.updateHEAD(mergedCommit.getUID());
    }


    /** Below are helper functions. */

    /** Delete files that are tracked in the current branch */
    public static void deleteTrackedFiles() {
        Commit currentCommit = Commit.fromUID(Branch.getHeadCommitUID());
        HashMap<String, String> currentTrackedBlobs = currentCommit.getTrackedBlobs();
        for (String filename : currentTrackedBlobs.keySet()) {
            if (!currentTrackedBlobs.containsKey(filename)) {
                restrictedDelete(filename);
            }
        }
    }

    /** save all blobs in given commit as files to CWD. */
    public static void checkoutFilesInCommit(String commitUID) {
        // If a working file is untracked in the current branch and would be overwritten by the checkout
        if (!getUntrackedFiles().isEmpty()) {
            System.out.println("There is an untracked file in the way; delete it, or add and commit it first.");
            // return;
        }
        Commit commit = Commit.fromUID(commitUID);
        HashMap<String, String> trackedBlobs = commit.getTrackedBlobs();
        for (String filename : trackedBlobs.keySet()) {
            Blob blob = Blob.fromUID(trackedBlobs.get(filename));
            blob.writeToFile(filename);
        }
    }

    /** get allfiles present in CWD but neither staged for addition nor tracked. */
    public static List<String> getUntrackedFiles() {
        Commit currentCommit = Commit.fromUID(Branch.getHeadCommitUID());
        HashMap<String, String> currentTrackedBlobs = currentCommit.getTrackedBlobs();
        StagingArea STAGING_AREA = StagingArea.load();

        List<String> untrackedFiles = new ArrayList<>();
        File[] files = CWD.listFiles();
        for (File file : files) {
            if (file.isFile() && !STAGING_AREA.containsFilename(file.getName())
                    && !currentTrackedBlobs.containsKey(file.getName())) {
                untrackedFiles.add(file.getName());
            }
        }
        return untrackedFiles;
    }

    /** get all modified but not staged files present in CWD.
     * Tracked in the current commit, changed in the working directory, but not staged; or
     * Staged for addition, but with different contents than in the working directory; or
     * Staged for addition, but deleted in the working directory; or
     * Not staged for removal, but tracked in the current commit and deleted from the working directory.
     * "I should have unified the API!" */
    public static List<String> getModifiedFiles() {
        Commit currentCommit = Commit.fromUID(Branch.getHeadCommitUID());
        HashMap<String, String> currentTrackedBlobs = currentCommit.getTrackedBlobs();
        StagingArea STAGING_AREA = StagingArea.load();
        List<String> modifiedFiles = new ArrayList<>();
        File[] files = CWD.listFiles();

        // Tracked in the current commit, changed in the working directory, but not staged;
        for (String filename : currentTrackedBlobs.keySet()) {
            //System.out.println("wowowow" + filename);
            boolean inCWD = false;
            for (File file : files) {
                if (file.isFile() && file.getName().equals(filename)) {
                    inCWD = true;
                    Blob blob = Blob.fromUID(currentTrackedBlobs.get(filename));
                    if (!blob.hasEqualContent(file)) {
                        modifiedFiles.add(filename);
                    }
                }
            }
            // Not staged for removal, but tracked in the current commit and deleted from the working directory.
            if (!inCWD && !STAGING_AREA.containsFilename(filename)) {
                modifiedFiles.add(filename);
            }
        }

        // Staged for addition, but with different contents than in the working directory
        for (String filename : STAGING_AREA.getFilename()) {
            boolean inCWD = false;
            for (File file : files) {
                if (file.isFile() && file.getName().equals(filename)) {
                    inCWD = true;
                    Blob blob = STAGING_AREA.getBlob(filename);
                    if (!blob.hasEqualContent(file)) {
                        modifiedFiles.add(filename);
                    }
                }
            }
            // Staged for addition, but deleted in the working directory;
            if (!inCWD) {
                modifiedFiles.add(filename);
            }
        }

        return modifiedFiles;
    }

}