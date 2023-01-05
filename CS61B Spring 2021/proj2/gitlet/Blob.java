package gitlet;

import java.io.File;
import java.io.Serializable;
import java.nio.charset.StandardCharsets;

public class Blob implements Serializable {
    private final String UID;
    private final byte[] content;

    public Blob(File file) {
        String name = file.getName();
        this.content = Utils.readContents(file);
        this.UID = Utils.sha1(name, content);
    }

    public String getUID() {
        return UID;
    }

    public String getContentAsString() {
        return new String(content, StandardCharsets.UTF_8);
    }

    public void dump() {
        File folder = new File(".gitlet/objects/" + UID.substring(0, 2) + "/");
        File file = Utils.join(folder, UID.substring(2, 42));
        Utils.writeObject(folder, this);
    }

    public static Blob fromFile(File file) {
        return Utils.readObject(file, Blob.class);
    }
}
