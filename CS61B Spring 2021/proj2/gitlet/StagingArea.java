package gitlet;

import java.io.File;
import java.io.Serializable;
import java.util.HashMap;
import java.util.HashSet;


/** Staging area for gitlet.
 * stores the UID of the files that are staged for addition and removal.
 * */
public class StagingArea implements Serializable {
    /** The files to be added. */
    private final HashSet<String> addition;
    /** The files to be removed. */
    private final HashSet<String> removal;
    /** The location of the staging area. */
    private final File INDEX = new File(".gitlet/index");
    /** The files that are in the staging area. key is the UID, value is the filenames*/
    private final HashMap<String, String> files;

    public StagingArea() {
        this.addition = new HashSet<>();
        this.removal = new HashSet<>();
        this.files = new HashMap<>();
    }

    public HashSet<String> getAddition() {
        return this.addition;
    }

    public HashSet<String> getRemoval() {
        return this.removal;
    }

    public void addBlob(Blob blob) {
        String UID = blob.getUID();
        if (removal.contains(UID)) {
            removal.remove(UID);
        }
        addition.add(UID);
        files.put(UID, blob.getFilename());
    }

    public void removeBlob(Blob blob) {
        String UID = blob.getUID();
        if (addition.contains(UID)) {
            addition.remove(UID);
        }
        removal.add(UID);
        files.put(UID, blob.getFilename());
    }

    public void dump() {
        Utils.writeObject(INDEX, this);
    }

    public static StagingArea fromFile(File file) {
        return Utils.readObject(file, StagingArea.class);
    }
}
