#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long cc;
    int i = 0;
    int luhn = 0;
    int n;
    int mark1;
    int mark2;
    do
    {
        cc = get_long_long("Number: ");
    }
    while (cc <= 0);

    //count length
    for (long long cc1 = cc; cc1 > 0 ; cc1 = cc1 / 10)
    {
        i++;
        if (cc1 < 10)
        {
            mark1 = cc1;
        }
        else if (cc1 < 100)
        {
            mark2 = cc1;
        }
    }

    //compute luhn
    for (long long cc1 = cc; cc1 > 0 ; cc1 = cc1 / 100)
    {
        luhn = luhn + cc1 % 10;
    }
    for (long long cc1 = cc / 10; cc1 > 0 ; cc1 = cc1 / 100)
    {
        n = cc1 % 10;
        n = n * 2;
        if (n >= 10)
        {
            luhn = luhn + n / 10 + n % 10;
        }
        else
        {
            luhn = luhn + n;
        }
    }

    // identify company
    if (luhn % 10 == 0)
    {
        if ((mark1 == 4) && ((i == 13) || (i == 16)))
        {
            printf("VISA\n");
        }
        else if (((mark2 == 34) || (mark2 == 37)) && (i == 15))
        {
            printf("AMEX\n");
        }
        else if (((51 <= mark2) && (mark2 <= 55)) && (i == 16))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
