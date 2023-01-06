package gitlet;

import java.io.File;
import java.io.Serializable;
import java.util.HashSet;


/** Staging area for gitlet.
 * stores the UID of the files that are staged for addition and removal.
 * */
public class StagingArea implements Serializable {
    /** The files to be added. */
    private final HashSet<String> addition;
    /** The files to be removed. */
    private final HashSet<String> removal;
    private final File INDEX = new File(".gitlet/index");

    public StagingArea() {
        this.addition = new HashSet<>();
        this.removal = new HashSet<>();
    }

    public HashSet<String> getAddition() {
        return this.addition;
    }

    public HashSet<String> getRemoval() {
        return this.removal;
    }

    public void addBlob(String UID) {
        if (removal.contains(UID)) {
            removal.remove(UID);
        }
        addition.add(UID);
    }

    public void removeBlob(String UID) {
        if (addition.contains(UID)) {
            addition.remove(UID);
        }
        removal.add(UID);
    }

    public void dump() {
        Utils.writeObject(INDEX, this);
    }

    public static StagingArea fromFile(File file) {
        return Utils.readObject(file, StagingArea.class);
    }
}
