package gitlet;

import java.io.File;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;

/** Represents a gitlet commit object.
 *  @author hdx
 */
public class Commit implements Dumpable {
    /** The message of this Commit. */
    private String message;
    /** The time of this Commit. */
    private Date timestamp;
    /** The parent of this Commit. We use string not Commit to avoid serialize problem*/
    private String parent;
    /** If there is a branch split and merge, we need to store the second parent. */
    private String secondParent;
    /** The pointer points to the filename and UID pairs of the blob of current Commit.
     * We use HashMap rather than HashSet since it is troublesome to index the blob and get the filename
     * in that blob. (Maybe it is in the staging area or in the object dir.)
     * KEY: filename; value: UID (we don't want conflict of the filename) */
    private HashMap<String, String> trackedBlobs;
    /** The UID of this Commit. */
    private String UID;

    public Commit(String message, HashMap<String, String> trackedBlobs, String parent) {
        this.message = message;
        if (trackedBlobs == null) {
            this.trackedBlobs = new HashMap<>();
        } else {
            this.trackedBlobs = trackedBlobs;
        }
        this.parent = parent;
        if (parent == null) {
            this.timestamp = new Date(0);
            this.UID = Utils.sha1(message, timestamp.toString(), null, null);
        } else {
            this.timestamp = new Date();
            this.UID = Utils.sha1(message, timestamp.toString(), parent, trackedBlobs.toString());
        }
    }

    public String getMessage() {
        return this.message;
    }

    public Date getTimestamp() {
        return this.timestamp;
    }

    public HashMap<String, String> getTrackedBlobs() {
        return this.trackedBlobs;
    }

    public String getParent() {
        return this.parent;
    }

    /** Add blobs to the trackedBlobs. */
    public void addBlobs(HashSet<Blob> blobs) {
        for (Blob blob : blobs) {
            this.trackedBlobs.put(blob.getFilename(), blob.getUID());
        }
    }

    public String getUID() {
        return this.UID;
    }

    /** Update this commit. */
    public void update(HashSet<Blob> blobs, String message) {
        this.message = message;
        this.addBlobs(blobs);
        this.timestamp = new Date();
        this.parent = this.UID;
        this.UID = Utils.sha1(message, timestamp.toString(), parent, trackedBlobs.toString());
        this.dump();
    }

    public void dump() {
        File folder = new File(Repository.OBJECT_DIR + "/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            folder.mkdirs();
        }
        Utils.writeObject(file, this);
    }

    public static Commit fromFile(File file) {
        return Utils.readObject(file, Commit.class);
    }

    /** Return the commit with the given UID, or null if it doesn't exist. */
    public static Commit fromUID(String UID) {
        File folder = new File(Repository.OBJECT_DIR + "/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            return null;
        }
        return Utils.readObject(file, Commit.class);
    }

    /** Find the UID of all commits that have the given commit message. */
    public static HashSet<String> findWithMsg(String message) {
        HashSet<String> result = new HashSet<>();
        File folder = new File(".gitlet/objects/");
        for (File file : folder.listFiles()) {
            if (file.isDirectory()) {
                for (File file1 : file.listFiles()) {
                    Commit commit = Utils.readObject(file1, Commit.class);
                    if (commit.getMessage().equals(message)) {
                        result.add(commit.getUID());
                    }
                }
            }
        }
        return result;
    }

    public void printLog() {
        System.out.println("===");
        System.out.println("commit " + this.getUID());
        System.out.println("Date: " + this.getTimestamp());
        System.out.println(this.getMessage());
        System.out.println();
    }

    public static void checkExists(String commitID) {
        if (Commit.fromUID(commitID) == null) {
            Utils.exitWithError("No commit with that id exists.");
        }
    }
}
