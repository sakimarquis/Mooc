//输入明文和密匙，把明文转化为ascii code，然后加减密匙，得到密文。

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

//开始输入代码时得到一个key值
int main(int argc, string argv[])
{
    //argc参数必须是2,不然return 1报错
    if (argc != 2)
    {
        printf("error");
        return 1;
    }

    //将输入的值转为整数
    int k = atoi(argv[1]);

    //如果K是非负整数，不然return 1报错
    if (k < 0)
    {
        printf("error");
        return 1;
    }

    //获取明文
    string n = get_string("plaintext: ");

    //转换
    for (int i = 0; i < strlen(n); i++)
    {
        //判断是不是字母
        if (isalpha(n[i]))
        {
            //判断大小写后转换
            if (isupper(n[i]))
            {
                n[i] = ((int)n[i] + k - 65) % 26 + 65;
            }
            if (islower(n[i]))
            {
                n[i] = ((int)n[i] + k - 97) % 26 + 97;
            }
        }
    }

    //密文
    printf("ciphertext: %s\n", n);
}
