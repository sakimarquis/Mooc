package gitlet;

import java.io.File;
import java.io.Serializable;
import java.util.Date;
import java.util.HashSet;

/** Represents a gitlet commit object.
 *  @author hdx
 */
public class Commit implements Serializable {
    /** The message of this Commit. */
    private final String message;
    /** The time of this Commit. */
    private final Date timestamp;
    /** The parent of this Commit. We use string not Commit to avoid serialize problem*/
    private final String parent;
//    /** The pointer points to the UID of the blob of this Commit. */
//    private final HashSet<String> trackedBlobsUID;
    /** The UID of this Commit. */
    private final String UID;

    public Commit(String message, HashSet<String> trackedBlobsUID, String parent) {
        this.message = message;
        this.parent = parent;
        if (parent == null) {
            this.timestamp = new Date(0);
            this.UID = Utils.sha1(message, timestamp.toString(), null, null);
        } else {
            this.timestamp = new Date();
            this.UID = Utils.sha1(message, timestamp.toString(), parent, trackedBlobsUID.toString());
        }
    }

    public String getMessage() {
        return this.message;
    }

    public Date getTimestamp() {
        return this.timestamp;
    }

    public String getParent() {
        return this.parent;
    }

    public String getUID() {
        return this.UID;
    }

//    public HashSet<String> getTrackedBlobsUID() {
//        return this.trackedBlobsUID;
//    }
//
//    public void addBlobsUID(String[] files) {
//        for (String file : files) {
//            Blob blob = new Blob(new File(file));
//            this.trackedBlobsUID.add(blob.getUID());
//        }
//    }

    public void dump() {
        File folder = new File(".gitlet/objects/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, 40));
        if (!folder.exists()) {
            folder.mkdirs();
        }
        Utils.writeObject(file, this);
    }

    public static Commit fromFile(File file) {
        return Utils.readObject(file, Commit.class);
    }
}
