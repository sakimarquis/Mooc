package gitlet;

import java.io.File;

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
}
