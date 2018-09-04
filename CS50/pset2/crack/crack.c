#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <crypt.h>
#include <ctype.h>

//命令得到hashed value
int main(int argc, string argv[])
{
    //argc参数必须是2,不然return 1报错
    if (argc != 2)
    {
        printf("Error");
        return 1;
    }
    
    //找出salt
    char salt[3];
    strncpy(salt, argv[1], 2);
    
    
    
    
    if (strcmp(crypt(passwd, salt), argv[1]) == 0)
    {
        printf("%s\n", passwd);
        return 0;
    }
}
