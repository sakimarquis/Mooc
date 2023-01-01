package gh2;
import edu.princeton.cs.algs4.StdRandom;

public class DrumString extends GuitarString {
    private static final double DECAY = 1;
    public DrumString(double frequency) {
        super(frequency);
    }

    @Override
    public void tic() {
        double first = buffer.removeFirst();
        double second = buffer.get(0);
        int rd = StdRandom.uniform(0, 2);
        if (rd == 0) {
            buffer.addLast((first + second) / 2 * DECAY);
        } else {
            buffer.addLast(- (first + second) / 2 * DECAY);
        }
    }
}
