package gitlet;

import java.io.File;
import java.io.Serializable;
import java.util.HashSet;


/** Staging area for gitlet.
 * stores the UID of the files that are staged for addition and removal.
 * */
public class StagingArea implements Dumpable {
    /** The files to be added. */
    private final HashSet<String> additionUID;
    /** The files to be removed. */
    private final HashSet<String> removalUID;
    /** The location of the staging area. */
    private static final File INDEX_DIR = new File(".gitlet/index");
    /** The files that are in the staging area. key is the UID, value is the blob*/
    private final HashSet<Blob> blobs;

    public StagingArea() {
        this.additionUID = new HashSet<>();
        this.removalUID = new HashSet<>();
        this.blobs = new HashSet<>();
    }

    public HashSet<String> getAdditionUID() {
        return this.additionUID;
    }

    public HashSet<String> getRemovalUID() {
        return this.removalUID;
    }

    public HashSet<Blob> getStagedBlobs() {
        return this.blobs;
    }

    public void addBlob(Blob blob) {
        String UID = blob.getUID();
        if (removalUID.contains(UID)) {
            removalUID.remove(UID);
        }
        additionUID.add(UID);
        blobs.add(blob);
    }

    public void removeBlob(Blob blob) {
        String UID = blob.getUID();
        if (additionUID.contains(UID)) {
            additionUID.remove(UID);
        }
        removalUID.add(UID);
    }

    /** Remove the blob from the staging area. */
    public void removeFromStagingArea(Blob blob) {
        String UID = blob.getUID();
        if (additionUID.contains(UID)) {
            additionUID.remove(UID);
            blobs.remove(blob);
        } else if (removalUID.contains(UID)) {
            removalUID.remove(UID);
        }
    }

    public void dump() {
        Utils.writeObject(INDEX_DIR, this);
    }

    public static StagingArea load() {
        return Utils.readObject(INDEX_DIR, StagingArea.class);
    }
}
