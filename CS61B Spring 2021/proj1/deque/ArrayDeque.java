package deque;

public class ArrayDeque<T> {
    private T[] items;
    private int size;
    private int first;
    private int last;
    private final int SIZE = 8;

    public ArrayDeque() {
        items = (T[]) new Object[SIZE];
        size = 0;
        first = SIZE / 2 - 1;
        last = SIZE / 2;
    }

    public void addFirst(T item) {
        if (size == items.length) {
            resize(size * 2);
        }
        items[size] = item;
        first -= 1;
        size += 1;
    }

    public void addLast(T item) {
        if (size == items.length) {
            resize(size * 2);
        }
        items[size] = item;
        last += 1;
        size += 1;
    }

    private void resize(int capacity) {
        T[] tmp = (T[]) new Object[capacity];
        int new_first = capacity / 4;
        System.arraycopy(items, first, tmp, new_first, size);
        first = new_first;
        last = first + size + 1;
        items = tmp;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void printDeque() {
        for (int i = first; i < last; i++) {
            System.out.print(items[i] + " ");
        }
        System.out.println();
    }

    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        T item = items[first];
        items[first] = null;
        first += 1;
        size -= 1;
        if (size <= items.length / 4) {
            resize(size * 2);
        }
        return item;
    }

    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        T item = items[last];
        items[last] = null;
        last -= 1;
        size -= 1;
        if (size <= items.length / 4) {
            resize(size * 2);
        }
        return item;
    }
}
