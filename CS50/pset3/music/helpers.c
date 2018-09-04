// Helper functions for music

#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include "helpers.h"
#include <string.h>
#define DEFAULT_TONE 4
#define DEFAULT_FREQUENCY 440

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    return 8 * (fraction[0] - '0') / (fraction[2] - '0');
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    float count = 0;
    if (strlen(note) == 2)
    {
        count = count + ((note[1] - '0') - DEFAULT_TONE) * 12;
    }
    else
    {
        if (note[1] == '#')
        {
            count++;
        }
        if (note[1] == 'b')
        {
            count--;
        }
        count = count + ((note[2] - '0') - DEFAULT_TONE) * 12;
    }
    
    //hardcode!!!!!!!
    if (note[0] == 'C')
    {
        count = count - 9;
    }
    if (note[0] == 'D')
    {
        count = count - 7;
    }    
    if (note[0] == 'E')
    {
        count = count - 5;
    }    
    if (note[0] == 'F')
    {
        count = count - 4;
    }    
    if (note[0] == 'G')
    {
        count = count - 2;
    }    
    if (note[0] == 'B')
    {
        count = count + 2;
    }
    return round(DEFAULT_FREQUENCY * pow(2, count / 12));
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strlen(s) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}