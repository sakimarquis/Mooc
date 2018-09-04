#include <stdio.h>
#include <math.h>

int main(void)
{
    float f = 0.0999999999;
    f = round(f);
    printf("%.3f\n", f);
}