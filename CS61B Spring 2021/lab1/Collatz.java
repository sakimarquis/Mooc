/** Class that prints the Collatz sequence starting from a given number.
 *  @author hdx
 */
public class Collatz {

    /** Buggy implementation of nextNumber! */
    public static int nextNumber(int n) {
        if (n == 1) {
            return 1;
        } else if (n % 2 == 1) {
            return 3 * n + 1;
        } else if (n % 2 == 0) {
            return n / 2;
        }
        return 0;
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.print(n + " ");
        while (n != 1) {
            n = nextNumber(n);
            System.out.print(n + " ");
        }
        System.out.println();
    }
}

