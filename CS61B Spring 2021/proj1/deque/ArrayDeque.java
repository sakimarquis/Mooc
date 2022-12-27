package deque;

public class ArrayDeque<T> {
    private T[] items;
    private int size;
    public int first;
    public int last;

    public ArrayDeque() {
        int SIZE = 8;
        items = (T[]) new Object[SIZE];
        size = 0;
        first = SIZE / 2;
        last = SIZE / 2;
    }

    private int getCircularPointer(int pointer) {
        if (pointer < 0) {
            return pointer + items.length;
        } else if (pointer >= items.length) {
            return pointer - items.length;
        } else {
            return pointer;
        }
    }

    public void addFirst(T item) {
        if (size == items.length) {
            resize(size * 2);
        }
        size += 1;
        if (size > 1) {
            first = getCircularPointer(first - 1);
        }
        items[first] = item;
    }

    public void addLast(T item) {
        if (size == items.length) {
            resize(size * 2);
        }
        size += 1;
        if (size > 1) {
            last = getCircularPointer(last + 1);
        }
        items[last] = item;
    }

    private void resize(int capacity) {
        T[] tmp = (T[]) new Object[capacity];
        int new_first = capacity / 4;
        System.arraycopy(items, 0, tmp, new_first, size);
        items = tmp;
        first = new_first;
        last = getCircularPointer(first + size - 1);
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
        size -= 1;
        if (size > 0) {
            last = getCircularPointer(last - 1);
        }
        if (size <= items.length / 4 && items.length > 8) {
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
        size -= 1;
        if (size > 0) {
            last = getCircularPointer(last - 1);
        }
        if (size <= items.length / 4 && items.length > 8) {
            resize(size * 2);
        }
        return item;
    }

    public T get(int index) {
        if (index >= size) {
            return null;
        } else {
            int real_index = getCircularPointer(first + index);
            return items[real_index];
        }
    }
}
