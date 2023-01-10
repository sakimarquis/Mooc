package gitlet;

import java.io.File;
import java.util.Collection;
import java.util.HashMap;
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
    /** The files that are in the staging area. key is the filename, value is the blob*/
    private final HashMap<String, Blob> blobs;

    public StagingArea() {
        this.additionUID = new HashSet<>();
        this.removalUID = new HashSet<>();
        this.blobs = new HashMap<>();
    }

    public HashSet<String> getAdditionUID() {
        return this.additionUID;
    }

    public HashSet<String> getRemovalUID() {
        return this.removalUID;
    }

    public HashSet<Blob> getStagedBlobs() {
        Collection<Blob> blobs = this.blobs.values();
        return new HashSet<>(blobs);
    }

    public void addBlob(Blob blob) {
        String UID = blob.getUID();
        if (removalUID.contains(UID)) {
            removalUID.remove(UID);
        }
        additionUID.add(UID);
        blobs.put(blob.getFilename(), blob);
    }

    public void removeBlob(Blob blob) {
        String UID = blob.getUID();
        if (additionUID.contains(UID)) {
            additionUID.remove(UID);
        }
        removalUID.add(UID);
    }

    public void removeBlob(String UID) {
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
            blobs.remove(blob.getFilename());
        } else if (removalUID.contains(UID)) {
            removalUID.remove(UID);
        }
    }

    public void dump() {
        Utils.writeObject(INDEX_DIR, this);
    }

    public HashSet<Blob> getRemovalBlob () {
        HashSet<Blob> removalBlob = new HashSet<>();
        StagingArea stagingArea = Utils.readObject(INDEX_DIR, StagingArea.class);
        for (String UID : stagingArea.getRemovalUID()) {
            Blob blob = Blob.fromUID(UID);
            removalBlob.add(blob);
        }
        return removalBlob;
    }

    public static StagingArea load() {
        return Utils.readObject(INDEX_DIR, StagingArea.class);
    }

    public static void clear() {
        StagingArea STAGING_AREA = new StagingArea();
        STAGING_AREA.dump();
    }

    public static Boolean isEmpty () {
        StagingArea stagingArea = Utils.readObject(INDEX_DIR, StagingArea.class);
        return stagingArea.getAdditionUID().isEmpty() && stagingArea.getRemovalUID().isEmpty();
    }

    public boolean containsFilename(String filename) {
        return blobs.containsKey(filename);
    }
}
