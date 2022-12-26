package randomizedtest;

import edu.princeton.cs.algs4.StdRandom;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Created by hug.
 */
public class TestBuggyAList {
    @Test
    public void testThreeAddThreeRemove() {
        AListNoResizing<Integer> L_naive = new AListNoResizing<>();
        BuggyAList<Integer> L_bug = new BuggyAList<>();
        for (int i = 4; i < 7; i++) {
            L_naive.addLast(i);
            L_bug.addLast(i);
        }

        for (int i = 4; i < 7; i++) {
            assertEquals(L_naive.removeLast(), L_bug.removeLast());
        }
    }

    @Test
    public void randomizedTest() {
        AListNoResizing<Integer> L = new AListNoResizing<>();
        BuggyAList<Integer> L_bug = new BuggyAList<>();

        int N = 10000;
        for (int i = 0; i < N; i += 1) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                // addLast
                int randVal = StdRandom.uniform(0, 100);
                L.addLast(randVal);
                L_bug.addLast(randVal);
                System.out.println("addLast(" + randVal + ")");
            } else if (operationNumber == 1) {
                // size
                int size = L.size();
                int size_bug = L_bug.size();
                System.out.println("size: " + size);
                assertEquals(size, size_bug);
            } else if (operationNumber == 2 && L.size() > 0) {
                // removeLast
                int last = L.removeLast();
                int last_bug = L_bug.removeLast();
                System.out.println("removeLast(): " + last);
                assertEquals(last, last_bug);
            } else if (operationNumber == 3 && L.size() > 0) {
                // getLast
                int last = L.getLast();
                int last_bug = L_bug.getLast();
                System.out.println("getLast(): " + last);
                assertEquals(last, last_bug);
            }
        }
    }
}
