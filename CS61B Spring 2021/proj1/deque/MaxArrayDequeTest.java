package deque;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Comparator;

/** Test the MaxArrayDeque, it should either tell you the max element in itself by using the Comparator<T> given to it
 * in the constructor, or an arbitrary Comparator<T> that is different from the one given in the constructor.*/
public class MaxArrayDequeTest {

    private static class stringComparator implements Comparator<String> {
        @Override
        public int compare(String x1, String x2) {
            return x1.compareTo(x2);
        }
    }

    public static Comparator<String> getStringComparator() {
        return new stringComparator();
    }

    private static class integerComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer x1, Integer x2) {
            return x1.compareTo(x2);
        }
    }

    public static Comparator<Integer> getIntegerComparator() {
        return new integerComparator();
    }

    private static class reverseIntegerComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer x1, Integer x2) {
            return x2.compareTo(x1);
        }
    }

    public static Comparator<Integer> getReverseIntegerComparator() {
        return new reverseIntegerComparator();
    }

    private static class stringLengthComparator implements Comparator<String> {
        @Override
        public int compare(String x1, String x2) {
            return x1.length() - x2.length();
        }
    }

    public static Comparator<String> getStringLengthComparator() {
        return new stringLengthComparator();
    }

    private static class strangeComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer x1, Integer x2) {
            return (x1 - x2) * 100 / (x1 + x2);
        }
    }

    public static Comparator<Integer> getStrangeComparator() {
        return new strangeComparator();
    }


    @Test
    public void testStringCompare() {
        Comparator<String> c = getStringComparator();
        MaxArrayDeque<String> L = new MaxArrayDeque<>(c);
        L.addLast("apple");
        L.addLast("banana");
        L.addLast("cat");
        L.addLast("dog");
        assertEquals("dog", L.max());
    }

    @Test
    public void testStringLengthCompare() {
        Comparator<String> c = getStringLengthComparator();
        MaxArrayDeque<String> L = new MaxArrayDeque<>(c);
        L.addLast("apple");
        L.addLast("banana");
        L.addLast("cat");
        L.addLast("dog");
        assertEquals("banana", L.max());
    }

    @Test
    public void testIntegerCompare() {
        Comparator<Integer> c = getIntegerComparator();
        MaxArrayDeque<Integer> L = new MaxArrayDeque<>(c);
        L.addLast(1);
        L.addLast(2);
        L.addLast(3);
        L.addLast(4);
        assertEquals(4, (int) L.max());
    }

    @Test
    public void testReverseIntegerCompare() {
        Comparator<Integer> c = getReverseIntegerComparator();
        MaxArrayDeque<Integer> L = new MaxArrayDeque<>(c);
        L.addLast(1);
        L.addLast(2);
        L.addLast(3);
        L.addLast(4);
        assertEquals(1, (int) L.max());
    }

    @Test
    public void testStrangeIntegerCompare() {
        Comparator<Integer> c = getStrangeComparator();
        MaxArrayDeque<Integer> L = new MaxArrayDeque<>(c);
        L.addLast(1);
        L.addLast(2);
        L.addLast(3);
        L.addLast(4);
        assertEquals(4, (int) L.max());
    }
}
