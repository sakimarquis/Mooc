package deque;

import org.junit.Test;
import static org.junit.Assert.*;


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
        L.addLast(1);
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
        L.addLast(1);
        L.addLast(2);
        L.addLast(3);
        L.addLast(4);
        L.addLast(5);
        L.addLast(6);
        assertEquals(1, (int) L.removeFirst());
        assertEquals(6, (int) L.removeLast());
        assertEquals(2, (int) L.removeFirst());
        assertEquals(5, (int) L.removeLast());
        assertEquals(3, (int) L.removeFirst());
        assertEquals(4, (int) L.removeLast());
    }

    @Test
    /* Tests resizing */
    public void resizeTest() {
        ArrayDeque<Integer> lld1 = new ArrayDeque<>();
        lld1.addFirst(3);
        lld1.addFirst(2);
        lld1.addFirst(1);
        lld1.addFirst(0);
        lld1.addFirst(-1);
        lld1.addFirst(-2);
        lld1.addFirst(-3);
        lld1.addFirst(-4);
        lld1.addFirst(-5);
        lld1.addFirst(-6);
        lld1.addFirst(-7);
        lld1.addFirst(-8);
        lld1.addFirst(-9);
        lld1.addFirst(-10);
    }
}
