package gitlet;

import java.io.File;
import static gitlet.Utils.*;


/** Represents a gitlet repository.
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
    /** The staging area. */
    private static StagingArea STAGING_AREA = new StagingArea();
    /** The current HEAD. */
    private static String HEAD = null;

    public static void init() {
        if (GITLET_DIR.exists()) {
            System.out.println("A Gitlet version-control system already exists in the current directory.");
            return;
        } else {
            GITLET_DIR.mkdir();
        }
        // Get the current working directory
        Commit initial = new Commit("initial commit", null, HEAD);
        HEAD = initial.getUID();
        initial.dump();
    }

    /** Adds a copy of the file as it currently exists to the staging area */
    public static void add(String filename) {
        File file = new File(filename);
        if (!file.exists()) {
            System.out.println("File does not exist.");
            return;
        }
        Blob blob = new Blob(file);
        STAGING_AREA.addBlob(blob);
        STAGING_AREA.dump();
    }

    /** Creates a new commit, saves tracked files in the current commit and staging Area. */
    public static void commit(String message) {
        if (message.equals("")) {
            System.out.println("Please enter a commit message.");
            return;
        }
        for (Blob blob : STAGING_AREA.getStagedBlobs()) {
            blob.dump();
        }
        Commit commit = new Commit(message, STAGING_AREA.getAdditionUID(), HEAD);
        commit.dump();
        STAGING_AREA = new StagingArea();  // clear the staging area
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
