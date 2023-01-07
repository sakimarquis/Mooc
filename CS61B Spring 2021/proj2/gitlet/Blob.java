package gitlet;

import java.io.File;
import java.io.Serializable;
import java.nio.charset.StandardCharsets;

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
        File folder = new File(".gitlet/objects/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, Utils.UID_LENGTH));
        if (!folder.exists()) {
            folder.mkdirs();
        }
        Utils.writeObject(file, this);
    }

    public static Blob fromFile(File file) {
        return Utils.readObject(file, Blob.class);
    }
}
