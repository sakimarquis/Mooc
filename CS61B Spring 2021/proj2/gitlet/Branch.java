package gitlet;

import java.io.File;



public class Branch implements Dumpable {

    public void dump() {
        File folder = new File(Repository.BRANCH_DIR + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            folder.mkdirs();
        }
        Utils.writeObject(file, this);
    }
}
