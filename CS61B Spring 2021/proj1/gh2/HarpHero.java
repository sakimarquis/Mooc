package gh2;
import deque.ArrayDeque;

public class HarpHero extends GuitarHero {
    public HarpHero() {
        musicStrings = new ArrayDeque<>();
        for (int i = 0; i < KEYBOARD_SIZE; i++) {
            double concert = 440.0 * Math.pow(2.0, (i - 24.0) / 12.0);
            MusicString s = new HarpString(concert);
            musicStrings.addLast(s);
        }
    }

    public static void main(String[] args) {
        HarpHero hh = new HarpHero();
        hh.play();
    }
}
