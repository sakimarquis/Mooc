#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float m;
    int i = 0;
    // ask for a non-negative float value
    do
    {
        m = get_float("Change owed: ");
    }
    while (m < 0);
    int n = round(m * 100);
    for (; n >= 25; n = n - 25)
    {
        i++;
    }
    for (; n >= 10; n = n - 10)
    {
        i++;
    }
    for (; n >= 5; n = n - 5)
    {
        i++;
    }
    for (; n >= 1; n = n - 1)
    {
        i++;
    }
    printf("%i\n", i);
}