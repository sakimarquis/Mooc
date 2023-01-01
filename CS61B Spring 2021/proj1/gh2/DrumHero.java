package gh2;
import deque.ArrayDeque;

public class DrumHero extends GuitarHero {
    public DrumHero() {
        musicStrings = new ArrayDeque<>();
        for (int i = 0; i < KEYBOARD_SIZE; i++) {
            double concert = 200.0 * Math.pow(2.0, (i - 24.0) / 12.0);
            MusicString s = new DrumString(concert);
            musicStrings.addLast(s);
        }
    }

    public static void main(String[] args) {
        DrumHero dh = new DrumHero();
        dh.play();
    }
}