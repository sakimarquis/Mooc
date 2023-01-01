package gh2;
import deque.ArrayDeque;
import deque.Deque;
import edu.princeton.cs.algs4.StdAudio;
import edu.princeton.cs.algs4.StdDraw;

/**
 * A client that uses the synthesizer package to replicate a plucked guitar string sound
 */
public class GuitarHero {
    private static final String KEYBOARD = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/' ";;
    private static final Integer KEYBOARD_SIZE = 37;
    private static Deque<GuitarString> GStrings;

    public static void main(String[] args) {
        GStrings = new ArrayDeque<>();
        for (int i = 0; i < KEYBOARD_SIZE; i++) {
            double concert = 440.0 * Math.pow(2.0, (i - 24.0) / 12.0);
            GuitarString s = new GuitarString(concert);
            GStrings.addLast(s);
        }
        while (true) {
            /* check if the user has typed a key; if so, process it */
            if (StdDraw.hasNextKeyTyped()) {
                char key = StdDraw.nextKeyTyped();
                int idx = KEYBOARD.indexOf(key);
                GuitarString gs = GStrings.get(idx);
                if (gs != null) {
                    gs.pluck();
                }
            }

            /* compute the superposition of samples */
            double sample = 0.0;
            for (int i = 0; i < KEYBOARD_SIZE; i++) {
                sample += GStrings.get(i).sample();
            }

            /* play the sample on standard audio */
            StdAudio.play(sample);

            /* advance the simulation of each guitar string by one step */
            for (int i = 0; i < KEYBOARD_SIZE; i++) {
                GStrings.get(i).tic();
            }
        }
    }
}
