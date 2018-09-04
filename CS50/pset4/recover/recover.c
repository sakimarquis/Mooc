//resize JEPG files
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCKSIZE 512

typedef uint8_t BYTE;

int main(int argc,char *argv[])
{
	//检测输入参数只有一个
	if (argc != 2)
	{
		fprintf(stderr,"Usage:./recovery file\n");
		return 1;
	}
	
	//定义变量，打开文件，无法打开提示错误并返回2
	char *infile = argv[1];
	BYTE currBlock[BLOCKSIZE];
	char filename[8];
	FILE *inptr = fopen(infile,"r");
	FILE *outptr;
	int count = 0;	
	if (inptr == NULL) 
	{
		fprintf(stderr,"Could not open %s.\n",infile);
		return 2;
	}
	
	//读文件，如果读不到512说明读到头了，结束循环
	while (fread(currBlock,BLOCKSIZE,1,inptr) != 0)
	{
		//满足JEPG头文件信息则创建新文件并打开
		if (currBlock[0] == 0xff && currBlock[1] == 0xd8 && currBlock[2] == 0xff && ((currBlock[3] & 0xf0) == 0xe0))
		{
			if (count > 0)
			{
				fclose(outptr);
			}
			sprintf(filename, "%03i.jpg", count);
			outptr = fopen(filename, "w");
			count ++;
		}
		if (count > 0)
        {
            fwrite(&currBlock, BLOCKSIZE, 1, outptr);
        }
	}
    fclose(outptr);
    fclose(inptr);
    return 0;
}
