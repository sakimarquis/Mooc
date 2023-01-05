package gitlet;


/** Driver class for Gitlet, a subset of the Git version-control system.
 *  @author hdx
 */
public class Main {

    /** Usage: java gitlet.Main ARGS, where ARGS contains
     *  <COMMAND> <OPERAND1> <OPERAND2> ... 
     */
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Must have at least one argument");
            System.exit(-1);
        }

        String firstArg = args[0];
        switch(firstArg) {
            case "init":
                Repository.init();
            case "add":
                Repository.add(args[1]);
            case "commit":
                break
            case "rm":
                break;
            case "log":
                break;
            case "global-log":
                break;
            case "find":
                break;
            case "status":
                break;
            case "checkout":
                break;
            case "branch":
                break;
            case "rm-branch":
                break;
            case "reset":
                break;
            case "merge":
                break;
        }
    }
}
