package deque;

public class ArrayDeque<T> implements Deque<T> {
    private T[] items;
    private int size;
    private int first;
    private int last;

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

    @Override
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

    @Override
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

    @Override
    public int size() {
        return size;
    }

    @Override
    public void printDeque() {
        for (int i = first; i < last; i++) {
            System.out.print(items[i] + " ");
        }
        System.out.println();
    }

    @Override
    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        T item = items[first];
        items[first] = null;
        size -= 1;
        if (size > 0) {
            first = getCircularPointer(first + 1);
        }
        if (size <= items.length / 4 && items.length > 8) {
            resize(size * 2);
        }
        return item;
    }

    @Override
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

    @Override
    public T get(int index) {
        if (index >= size) {
            return null;
        } else {
            int real_index = getCircularPointer(first + index);
            return items[real_index];
        }
    }

    @Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        } if (o instanceof ArrayDeque) {
            return equalsHelper((ArrayDeque) o);
        } else {
            return false;
        }
    }

    private boolean equalsHelper(ArrayDeque o) {
        if (this.size() != o.size()) {
            return false;
        } else {
            for (int i = 0; i < this.size(); i++) {
                if (this.get(i) != o.get(i)) {
                    return false;
                }
            }
            return true;
        }
    }
}
