package deque;

import java.util.Comparator;

public class MaxArrayDeque<T> extends ArrayDeque<T> {
    private Comparator<T> arrayComparator;
    public MaxArrayDeque(Comparator<T> c) {
        super();
        arrayComparator = c;
    }

    public T max() {
        if (isEmpty()) {
            return null;
        }
        T max = get(0);
        for (int i = 1; i < size(); i++) {
            T item = get(i);
            if (arrayComparator.compare(item, max) > 0) {
                max = item;
            }
        }
        return max;
    }
}
