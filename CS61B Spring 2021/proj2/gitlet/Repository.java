package gitlet;

import java.io.File;
import static gitlet.Utils.*;

// TODO: any imports you need here

/** Represents a gitlet repository.
 *  TODO: It's a good idea to give a description here of what else this Class
 *  does at a high level.
 *
 *  @author hdx
 */
public class Repository {
    /**
     * TODO: add instance variables here.
     *
     * List all instance variables of the Repository class here with a useful
     * comment above them describing what that variable represents and how that
     * variable is used. We've provided two examples for you.
     */

    /** The current working directory as File. */
    public static final File CWD = new File(System.getProperty("user.dir"));
    /** The .gitlet directory as File (DIR). */
    public static final File GITLET_DIR = join(CWD, ".gitlet");

    public static void init() {
        if (GITLET_DIR.exists()) {
            System.out.println("A Gitlet version-control system already exists in the current directory.");
        } else {
            GITLET_DIR.mkdir();
        }
        // Get the current working directory
        Commit initial = new Commit("initial commit", null, null);
        initial.dump();
    }

    /** Adds the file to the staging area. */
    public static void add(String filename) {
        File f = new File(filename);
        byte[] fileContents = readContents(f);
        String fileContentsString = Utils.sha1(fileContents);
        File stagingArea = join(GITLET_DIR, "stagingArea");
        File fileInStagingArea = join(stagingArea, filename);
        if (fileInStagingArea.exists()) {
            String fileInStagingAreaContents = readContentsAsString(fileInStagingArea);
            if (fileContentsString.equals(fileInStagingAreaContents)) {
                System.out.println("File has not been modified since the last commit.");
            } else {
                writeContents(fileInStagingArea, fileContents);
            }
        } else {
            writeContents(fileInStagingArea, fileContents);
        }
    }
//
//    public static void commit(String message) {
//        if (message.equals("")) {
//            System.out.println("Please enter a commit message.");
//        } else {
//            File stagingArea = join(GITLET_DIR, "stagingArea");
//            String[] files = stagingArea.list();
//            if (files.length == 0) {
//                System.out.println("No changes added to the commit.");
//            } else {
//                File head = join(GITLET_DIR, "head");
//                String headContents = readContentsAsString(head);
//                Commit parent = Commit.fromFile(new File(headContents));
//                Commit commit = new Commit(message, files, parent.getUID());
//                commit.dump();
//                writeContents(head, commit.getUID());
//                for (String file : files) {
//                    File fileInStagingArea = join(stagingArea, file);
//                    File fileInWorkingDir = join(CWD, file);
//                    writeContents(fileInWorkingDir, readContents(fileInStagingArea));
//                    fileInStagingArea.delete();
//                }
//            }
//        }
//    }
}
