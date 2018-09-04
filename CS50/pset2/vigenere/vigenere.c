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
        printf("Error Key");
        return 1;
    }

    int j = 0;

    //将输入的值转为string
    string k = argv[1];

    for (int i = 0; i < strlen(k); i++)
    {
        //判断是不是字母，并且转化为小写
        if (isalpha(k[i]))
        {
            k[i] = tolower(k[i]);
        }
        //如果key中存在非字母则报错
        else
        {
            printf("Error Key");
            return 1;
        }
    }

    //获取明文
    string n = get_string("plaintext: ");

    //转换
    for (int i = 0; i < strlen(n); i++)
    {
        if (j >= strlen(k))
        {
            j = j - strlen(k);
        }
        //判断是不是字母
        if (isalpha(n[i]))
        {
            //判断大小写后转换
            if (isupper(n[i]))
            {
                n[i] = ((int)n[i] - 65 + (int)k[j] - 97) % 26 + 65;
            }
            if (islower(n[i]))
            {
                n[i] = ((int)n[i] - 97 + (int)k[j] - 97) % 26 + 97;
            }
            j++;
        }
    }

    //密文
    printf("ciphertext: %s\n", n);
}
