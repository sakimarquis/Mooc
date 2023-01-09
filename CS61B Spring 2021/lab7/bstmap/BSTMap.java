package bstmap;

import java.util.Iterator;
import java.util.Set;

public class BSTMap<K extends Comparable<K>, V> implements Map61B<K, V> {
    private BSTMapNode root;
    private int size;

    private class BSTMapNode {
        private K key;
        private V value;
        private BSTMapNode left;
        private BSTMapNode right;

        public BSTMapNode(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    public void clear() {
        root = null;
        size = 0;
    }

    private BSTMapNode find(BSTMapNode T, K key) {
        if (T == null) {
            return null;
        }
        int cmp = key.compareTo(T.key);
        if (cmp == 0) {
            return T;
        } else if (cmp < 0) {
            return find(T.left, key);
        } else {
            return find(T.right, key);
        }
    }

    public boolean containsKey(K key) {
        return find(root, key) != null;
    }

    public V get(K key) {
        BSTMapNode T = find(root, key);
        if (T == null) {
            return null;
        } else {
            return T.value;
        }
    }

    public int size() {
        return size;
    }

    public void put(K key, V value) {
        root = put(root, key, value);
        size += 1;
    }

    private BSTMapNode put(BSTMapNode T, K key, V value) {
        if (T == null) {
            return new BSTMapNode(key, value);
        }
        int cmp = key.compareTo(T.key);
        if (cmp == 0) {
            T.value = value;
        }  else if (cmp < 0) {
            T.left = put(T.left, key, value);
        }  else {
            T.right = put(T.right, key, value);
        }
        return T;
    }

    public Set<K> keySet() {
        throw new UnsupportedOperationException();
    }

    public V remove(K key) {
        throw new UnsupportedOperationException();
    }

    public V remove(K key, V value) {
        throw new UnsupportedOperationException();
    }

    public Iterator<K> iterator() {
        return keySet().iterator();
    }
}
