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

    public static String getCommitUID(String branchName) {
        File file = Utils.join(Repository.BRANCH_DIR, "/" , branchName);
        if (!file.exists()) {
            return null;
        }
        Branch branch = Utils.readObject(file, Branch.class);
        return branch.commitUID;
    }

    public static void checkExists(String branchName) {
        File file = Utils.join(Repository.BRANCH_DIR, branchName);
        if (!file.exists()) {
            Utils.exitWithError("No such branch exists.");
        }
    }

    public static void checkCurrentBranch(String branchName) {
        if (Branch.getCommitUID(branchName).equals(readObject(Repository.HEAD_DIR, String.class))) {
            Utils.exitWithError("No need to checkout the current branch.");
        }
    }

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
        String HEAD = readObject(Repository.HEAD_DIR, String.class);
        // use DFS to search the latest common ancestor
        Commit headCommit = Commit.fromUID(HEAD);
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
}
