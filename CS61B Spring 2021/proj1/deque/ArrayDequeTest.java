package deque;

import org.junit.Test;
import static org.junit.Assert.*;
import edu.princeton.cs.algs4.StdRandom;


public class ArrayDequeTest {
    @Test
    public void testEmptySize() {
        ArrayDeque<Integer> L_i = new ArrayDeque<>();
        assertEquals(0, L_i.size());
        ArrayDeque<String> L_s = new ArrayDeque<>();
        assertEquals(0, L_s.size());
    }

    @Test
    public void testAddAndSize() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        L.addLast(1);
        assertEquals(1, L.size());
        L.addLast(2);
        assertEquals(2, L.size());
        L.addFirst(3);
        assertEquals(3, L.size());
        L.addLast(4);
        assertEquals(4, L.size());
        L.addFirst(5);
        assertEquals(5, L.size());
    }

    @Test
    public void testAddAndGet() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        L.addLast(1);
        assertEquals(1, (int) L.get(0));
        L.addLast(2);
        assertEquals(2, (int) L.get(1));
        L.addFirst(3);
        assertEquals(3, (int) L.get(0));
        L.addLast(4);
        assertEquals(4, (int) L.get(3));
        L.addFirst(5);
        assertEquals(5, (int) L.get(0));
    }

    @Test
    public void testGet() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        L.addFirst(1);
        L.addLast(2);
        L.addFirst(3);
        L.addLast(4);
        L.addFirst(5);
        assertEquals(5, (int) L.get(0));
        assertEquals(3, (int) L.get(1));
        assertEquals(1, (int) L.get(2));
        assertEquals(2, (int) L.get(3));
        assertEquals(4, (int) L.get(4));
    }

    @Test
    public void testRemove() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        for (int i = 1; i <= 6; i++) {
            L.addLast(i);
        }
        assertEquals(1, (int) L.removeFirst());
        assertEquals(6, (int) L.removeLast());
        assertEquals(2, (int) L.removeFirst());
        assertEquals(5, (int) L.removeLast());
        assertEquals(3, (int) L.removeFirst());
        assertEquals(4, (int) L.removeLast());
    }

    @Test
    public void testResizeNaive() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        for (int i = 0; i < 64; i++) {
            L.addLast(i);
        }
        for (int i = 0; i < 32; i++) {
            L.removeFirst();
            L.removeLast();
        }
    }

    @Test
    public void testRandomRun() {
        ArrayDeque<Integer> L = new ArrayDeque<>();
        int N = 10000;
        for (int i = 0; i < N; i += 1) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                int randVal = StdRandom.uniform(0, 100);
                L.addFirst(randVal);
                assertEquals(randVal, (int) L.get(0));
            } else if (operationNumber == 1) {
                int randVal = StdRandom.uniform(0, 100);
                L.addLast(randVal);
                int size = L.size();
                assertEquals(randVal, (int) L.get(size - 1));
            } else if (operationNumber == 2 && L.size() > 0) {
                L.removeFirst();
            } else if (operationNumber == 3 && L.size() > 0) {
                L.removeLast();
            }
        }
    }
}
