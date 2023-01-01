package gh2;

public class HarpString extends GuitarString {
    private static final double DECAY = -0.999;

    public HarpString(double frequency) {
        super(frequency);
    }

    @Override
    public void tic() {
        double first = buffer.removeFirst();
        double second = buffer.get(0);
        double newDouble = (first + second) / 2 * DECAY;
        buffer.addLast(newDouble);
    }
}
