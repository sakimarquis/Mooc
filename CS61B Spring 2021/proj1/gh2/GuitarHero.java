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
    public static final Integer KEYBOARD_SIZE = 37;
    public Deque<MusicString> musicStrings;

    public GuitarHero() {
        musicStrings = new ArrayDeque<>();
        for (int i = 0; i < KEYBOARD_SIZE; i++) {
            double concert = 440.0 * Math.pow(2.0, (i - 24.0) / 12.0);
            MusicString s = new GuitarString(concert);
            musicStrings.addLast(s);
        }
    }

    public void play() {
        while (true) {
            // check if the user has typed a key; if so, process it
            if (StdDraw.hasNextKeyTyped()) {
                // the user types this character
                char key = StdDraw.nextKeyTyped();
                int index = KEYBOARD.indexOf(key);
                if (index != -1) {
                    musicStrings.get(index).pluck();
                }
            }

            /* compute the superposition of samples */
            double sample = 0.0;
            for (int i = 0; i < KEYBOARD_SIZE; i++) {
                sample += musicStrings.get(i).sample();
            }

            /* play the sample on standard audio */
            StdAudio.play(sample);

            /* advance the simulation of each guitar string by one step */
            for (int i = 0; i < KEYBOARD_SIZE; i++) {
                musicStrings.get(i).tic();
            }
        }
    }
    public static void main(String[] args) {
        GuitarHero gh = new GuitarHero();
        gh.play();
    }
}
