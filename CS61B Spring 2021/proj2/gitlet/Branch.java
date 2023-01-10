package gitlet;

import java.io.File;

import static gitlet.Utils.readObject;

/** Represent the branch: pointer to the commit. */
public class Branch implements Dumpable {
    private final String branchName;
    private final String commitUID;

    public Branch(String branchName, String commitUID) {
        this.branchName = branchName;
        this.commitUID = commitUID;
    }

    public void dump() {
        File folder = Repository.BRANCH_DIR;
        if (!folder.exists()) {
            folder.mkdirs();
        }
        File file = Utils.join(folder, branchName);
        Utils.writeObject(file, this);
    }

    /** delete the branch. */
    public static void delete(String branchName) {
        File file = Utils.join(Repository.BRANCH_DIR, branchName);
        if (!file.exists()) {
            System.out.println("A branch with that name does not exist.");
            return;
        }
        file.delete();
    }

    /** given the branch name, get the branch file and return the commitUID it track. */
    public static String getCommitUID(String branchName) {
        File file = Utils.join(Repository.BRANCH_DIR, "/" , branchName);
        if (!file.exists()) {
            return null;
        }
        Branch branch = Utils.readObject(file, Branch.class);
        return branch.commitUID;
    }

    /** check whether the branch exists. */
    public static void checkExists(String branchName) {
        File file = Utils.join(Repository.BRANCH_DIR, branchName);
        if (!file.exists()) {
            Utils.exitWithError("No such branch exists.");
        }
    }

    /** Return the branch with the given branchName, or null if it doesn't exist. */
    public static boolean isBranchHEAD(String branchName) {
        return branchName.equals(readObject(Repository.HEAD_FILE, String.class));
    }

    /** Return the branch given the commitUID the branch track. */
    public static String getBranchNameFromUID(String branchUID) {
        File folder = Repository.BRANCH_DIR;
        for (File file : folder.listFiles()) {
            Branch branch = readObject(file, Branch.class);
            if (branch.commitUID.equals(branchUID)) {
                return branch.branchName;
            }
        }
        return null;
    }

    public static String findSplitPoint(String branchName) {
        // use DFS to search the latest common ancestor
        Commit headCommit = Commit.fromUID(getHeadCommitUID());
        while (headCommit != null) {
            Commit otherCommit = Commit.fromUID(Branch.getCommitUID(branchName));
            while (otherCommit != null) {
                if (headCommit.getUID().equals(otherCommit.getUID())) {
                    return headCommit.getUID();
                }
                otherCommit = Commit.fromUID(otherCommit.getParent());
            }
            headCommit = Commit.fromUID(headCommit.getParent());
        }
        return null;
    }

    /** Return the commit UID that the current HEAD points. */
    public static String getHeadCommitUID() {
        String headBranchName = readObject(Repository.HEAD_FILE, String.class);
        return Branch.getCommitUID(headBranchName);
    }

    /** Update current HEAD branch. */
    public static void updateHEAD(String commitUID) {
        String headBranchName = readObject(Repository.HEAD_FILE, String.class);
        Branch branch = new Branch(headBranchName, commitUID);
        branch.dump();
    }

    /** Change the HEAD to the given branchName. */
    public static void changeHEAD(String branchName) {
        Utils.writeObject(Repository.HEAD_FILE, branchName);
    }
}
