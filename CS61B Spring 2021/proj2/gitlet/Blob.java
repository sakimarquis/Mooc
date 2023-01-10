package gitlet;

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

/** Represents a gitlet blob object.
 * It is a file in the .gitlet/object directory. It has a file name and content.
 * We can use UID to retrieve it.
 *  @author hdx
 */
public class Blob implements Dumpable {
    private final String UID;
    private final byte[] content;
    private final String name;

    public Blob(File file) {
        this.name = file.getName();
        this.content = Utils.readContents(file);
        this.UID = Utils.sha1(name, content);
    }

    public Blob(String name, byte[] content) {
        this.name = name;
        this.content = content;
        this.UID = Utils.sha1(name, content);
    }

    public String getUID() {
        return UID;
    }

    public String getFilename() {
        return this.name;
    }

    public String getContentAsString() {
        return new String(content, StandardCharsets.UTF_8);
    }

    public void dump() {
        File folder = new File(Repository.OBJECT_DIR + "/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            folder.mkdirs();
        }
        Utils.writeObject(file, this);
    }

    public void writeToFile(String filename) {
        File file = Utils.join(Repository.CWD, "/", filename);
        Utils.writeContents(file, this.getContentAsString());
    }

    public static Blob fromFile(File file) {
        return Utils.readObject(file, Blob.class);
    }

    /** Return the commit with the given UID, or null if it doesn't exist. */
    public static Blob fromUID(String UID) {
        File folder = new File(Repository.OBJECT_DIR + "/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            return null;
        }
        return Blob.fromFile(file);
    }

    // Merge conflict files for Case 3.2, save the merged blob and return the UID.
    public static String merge(String currentBlobUID, String givenBlobUID) {
        Blob currentBlob = Blob.fromUID(currentBlobUID);
        Blob givenBlob = Blob.fromUID(givenBlobUID);
        String filename = currentBlob.getFilename();
        String currentContent = currentBlob.getContentAsString();
        String givenContent = givenBlob.getContentAsString();
        String mergedContent = "<<<<<<< HEAD" + System.lineSeparator() + currentContent + "======="
                + System.lineSeparator() + givenContent + ">>>>>>>" + System.lineSeparator();
        Blob mergedBlob = new Blob(filename, mergedContent.getBytes());
        mergedBlob.dump();
        return mergedBlob.getUID();
    }

    // Compare the content of this blob with the other file
    public boolean hasEqualContent(File file) {
        byte[] fileContent = Utils.readContents(file);
        return Arrays.equals(fileContent, this.content);
    }
}
