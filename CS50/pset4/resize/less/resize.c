//resize the BMP file

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h" 

int main(int argc,char *argv[])
{
	//检测命令栏输入的参数，如果不是4提示错误并返回1 
	if (argc != 4)
	{
		fprintf(stderr,"Usage:./resize n infile outfile\n");
		return 1;
	}

	//获取resize倍数，输入文件名，输出文件名 
	int resize = atoi(argv[1]);
	char *infile = argv[2]; 
	char *outfile = argv[3];

	//打开输入和输出文件，无法打开提示错误并返回2
	FILE *inptr = fopen(infile,"r");
	if (inptr == NULL) 
	{
		fprintf(stderr,"Could not open %s.\n",infile);
		return 1;
	}
	FILE *outptr = fopen(outfile,"w");
	if (outptr == NULL) 
	{
	    fclose(inptr);
		fprintf(stderr,"Could not open %s.\n",outfile);
		return 1;
	}

	//分别读取输入的BMP文件头和位图信息头，分别将文件信息缓存到bi和bf的地址，读取的大小为整个文件头的大小，读取一次
	BITMAPFILEHEADER bf;
	fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
	BITMAPINFOHEADER bi;
	fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

	//检测输入的BMP文件信息为24-bit无压缩BMP，如果不是则关闭文件报错返回4
	if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
	    bi.biBitCount != 24 || bi.biCompression != 0)
	{
		fclose(inptr);
        fclose(outptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 1;
	}

    //记录原图的Width和Height
    long oldbiWidth = bi.biWidth;
    long oldbiHeight = abs(bi.biHeight);

    //计算输入文件扫描行的padding
    //因为是24色，所以是1个像素占3个字节。位图宽度为像素，相乘为一个扫描行的字节数。
    //再除以4得到的余数则是多出来的字节，4减去这个再除以4，则是有多少个字节的padding。
    int inpadding = (4 - (oldbiWidth * sizeof(RGBTRIPLE)) % 4) % 4;
   
	//调整BMP文件头信息和位图信息
    bi.biWidth = bi.biWidth * resize;
	bi.biHeight = bi.biHeight * resize;
	int outpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;	
	bi.biSizeImage = ((bi.biWidth * sizeof(RGBTRIPLE)) + outpadding) * abs(bi.biHeight);
    bf.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + bi.biSizeImage;

	//写入BMP文件头信息和位图信息
	fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

	//缓存
    RGBTRIPLE triple;

	//列循环
	for (int i = 0; i < oldbiHeight; i++)
	{
		//重复resize列
		for (int n = 0; n < resize; n++)
		{
			//行循环
			for (int j = 0; j < oldbiWidth; j++)
			{
            	//读取输入文件的RGB信息，每次读RGB信息中的一个颜色字节
            	fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            	//在该行中重复resize次
            	for (int m = 0; m < resize; m++)
            	{
            		//写入输出文件的RGB信息
            		fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
            	}
			}

			//添加该行的padding
        	for (int k = 0; k < outpadding; k++)
        	{
            	fputc(0x00, outptr);
        	}

        	//把输入指针拨回去
        	fseek(inptr, -1 * oldbiWidth * sizeof(RGBTRIPLE), SEEK_CUR);
	    }
	    //跳过这行
        fseek(inptr,  oldbiWidth * sizeof(RGBTRIPLE) + inpadding, SEEK_CUR);   
    }
    //关闭文件，成功返回0
    fclose(inptr);
    fclose(outptr);
    return 0;
}