package gitlet;

import java.io.Serializable;

/** An interface describing dumpable objects.
 *  @author P. N. Hilfinger
 */
interface Dumpable extends Serializable {
    void dump();
}
