#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    int j;
    // ask a number range in 0~23
    do
    {
        n = get_int("Height:");
    }
    while (n < 0 || n > 23);
    // column
    for (int i = 0; i < n; i++)
    {
        // row
        for (j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("  ");
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

