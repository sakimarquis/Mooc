package timingtest;
import edu.princeton.cs.algs4.Stopwatch;

/**
 * Created by hug.
 */
public class TimeSLList {
    private static void printTimingTable(AList<Integer> Ns, AList<Double> times, AList<Integer> opCounts) {
        System.out.printf("%12s %12s %12s %12s\n", "N", "time (s)", "# ops", "microsec/op");
        System.out.printf("------------------------------------------------------------\n");
        for (int i = 0; i < Ns.size(); i += 1) {
            int N = Ns.get(i);
            double time = times.get(i);
            int opCount = opCounts.get(i);
            double timePerOp = time / opCount * 1e6;
            System.out.printf("%12d %12.2f %12d %12.2f\n", N, time, opCount, timePerOp);
        }
    }

    public static void main(String[] args) {
        timeGetLast(128001);
    }

    public static void timeGetLast(int size) {
        AList<Integer> Ns = new AList<>();
        AList<Double> times = new AList<>();
        AList<Integer> opCounts = new AList<>();
        SLList<Integer> L = new SLList<>();
        int OPS = 10000;

        for (int i = 1; i < size; i += 1) {
            L.addLast(0);
            if ((i % 1000 == 0) && ((i / 1000 & (i / 1000 - 1)) == 0)) {
                Stopwatch sw = new Stopwatch();
                for (int j = 1; j < OPS; j += 1) {
                    L.getLast();
                }
                double timeInSeconds = sw.elapsedTime();
                Ns.addLast(i);
                times.addLast(timeInSeconds);
                opCounts.addLast(OPS);
            }
        }
        printTimingTable(Ns, times, opCounts);
    }

}
