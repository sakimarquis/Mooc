public class maxArray {
    /** Returns the maximum value from m. */
    public static int max(int[] m) {
        int max_val = -9999;
        int i = 0;
        while (i < m.length) {
            if (m[i] > max_val) {
                max_val = m[i];
            }
            i = i + 1;
        }
        return max_val;
    }
    public static void main(String[] args) {
        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
        System.out.println(max(numbers));
    }
}
