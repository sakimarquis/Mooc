public class TriangleDrawer {
    public static void drawTriangle(int SIZE) {
        int row = 0;
        while (row < SIZE) {
            int col = 0;
            while (col <= row) {
                System.out.print("*");
                col = col + 1;
            }
            System.out.println();
            row = row + 1;
        }
    }

    public static void main(String[] args) {
        drawTriangle(10);
    }
}
