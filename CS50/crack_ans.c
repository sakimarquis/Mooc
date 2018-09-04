// crack.c
// Brute force method of cracking short passwords

#include <cs50.h>
#include <stdio.h>
#include <unistd.h>
#include <crypt.h>
#include <string.h>

// Useful constants
#define MAX_LEN 5
#define SALT_LEN 2

int main(int argc, string argv[])
{
    // Alert user if usage is wrong
    if (argc != 2)
    {
        printf("Usage: %s <hash>", argv[0]);
        return 1;
    }

    // Get the salt portion of the hash (typically "50")
    string hash = argv[1];
    char salt[SALT_LEN + 1];
    strncpy(salt, hash, SALT_LEN);

    // Initialize the current guess as all null terminators
    char cur_guess[MAX_LEN + 1];
    for (int cur_char = 0; cur_char < (MAX_LEN + 1); cur_char++)
    {
        cur_guess[cur_char] = '\0';
    }

    // Continually increment the left-most letter, rolling over odometer-style if needed
    int increment_location = 0;
    bool rolling_over;

    // Repeat until we've cycled through all combos of every position
    while (increment_location < MAX_LEN)
    {
        // Not currently rolling over
        rolling_over = false;

        // Advance through the characters, jumping through ASCII as needed
        switch (cur_guess[increment_location])
        {
            // Null terminators tick up to 'a'
            case '\0':
                cur_guess[increment_location] = 'a';
                break;

            // 'z' ticks up to 'A'
            case 'z':
                cur_guess[increment_location] = 'A';
                break;

            // 'Z' rolls over the ticker, and goes back to 'a'
            case 'Z':
                cur_guess[increment_location] = 'a';
                increment_location++;
                rolling_over = true;
                break;

            // Otherwise, advance one character in ASCII as expected
            default:
                cur_guess[increment_location]++;
        }

        // Unless we're in the middle of a tick-over, check the guess.
        if (!rolling_over)
        {
            // If no difference between our guess and the actual password, we cracked it.
            if (strcmp(crypt(cur_guess, salt), hash) == 0)
            {
                printf("%s\n", cur_guess);
                return 0;
            }

            // Reset to incrementing the leftmost position, since we're done rolling over
            increment_location = 0;
        }
    }

    // Not able to crack
    printf("Unable to crack this password.\n");
    return 2;
}
