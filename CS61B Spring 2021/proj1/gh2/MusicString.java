package gh2;

public interface MusicString {
    /* Pluck the guitar string by replacing the buffer with white noise. */
    void pluck();

    /* Advance the simulation one time step by performing one iteration of
     * the Karplus-Strong algorithm.
     */
    void tic();

    /* Return the double at the front of the buffer. */
    double sample();
}
