// resize.c
// Resizes a bitmap by a factor in (0.0, 100.0)

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: resize f infile outfile\n");
        return 1;
    }

    // parse the float arg, just as get_float does in cs50.h
    float factor;
    char c;
    if (sscanf(argv[1], "%f %c", &factor, &c) != 1)
    {
        printf("n, the resize factor, must be a float\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // range check: n must be on (0.0, 100.0)
    if (factor <= 0 || factor > 100)
    {
        printf("The resize factor, must satisfy 0 < n <= 100.\n");
        return 1;
    }

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        printf("Could not create %s.\n", outfile);
        return 1;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        printf("Unsupported file format.\n");
        return 1;
    }

    // width of original for future reference
    int oldWidth = bi.biWidth;

    // determine padding for scanlines of original
    int oldPadding = (4 - (oldWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // update BITMAPINFOHEADER with dimensions after resize
    bi.biWidth *= factor;
    bi.biHeight *= factor;

    // determine padding for scanlines of resized image
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // update BITMAPINFOHEADER with new image size
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + padding) * abs(bi.biHeight);

    // update BITMAPFILEHEADER with new bitmap file size
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER)
                + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER and BITMAPINFOHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // currRow stores one of the rows in the input picture.
    // rowNum states which row is being stored.
    RGBTRIPLE currRow[oldWidth];
    int rowNum = -1;

    // iterate over every pixel in outfile, and find and write
    // the new color.
    for (int y = 0; y < abs(bi.biHeight); y++)
    {
        // Nearest neighbors.  All of the pixels on one
        // outfile row will draw from the pixels of one row
        // in the infile.  Find out what row that should be and
        // load it into currRow, if we haven't already.
        // oldY变量的意思是，输出的第y行是原来输入图片的第y/factor行
        int oldY = y / factor;

        // if we don't already have the correct row loaded, then seek to the
        // desired row and read it in to our buffer
        // 这里就是在尝试在infile中，找到第oldY行或者近似的行
        if (rowNum != oldY)
        {
            // we want to skip over the headers and oldY rows, where each row
            // has oldWidth pixels and oldPadding bytes of padding
            // 跳过oldY行前面的数据
            size_t pos = (sizeof(RGBTRIPLE) * oldWidth + oldPadding) * oldY +
                         sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
            
            //在输入文件中放置指针，指针的位置在文件开头偏移pos量的位置
            fseek(inptr, pos, SEEK_SET);
            rowNum = oldY;
            //读取这一行，一直读到padding，将信息存在currRow地址中
            fread(&currRow, sizeof(RGBTRIPLE), oldWidth, inptr);
        }

        // Draw the pixels in that row into the output.
        // 写bi.biWidth个
        for (int x = 0; x < bi.biWidth; x++)
        {
            //在读取的这一行（也就是对应的这一行）中，得到第x/factor列数据，四舍五入
            RGBTRIPLE triple = currRow[(int) (x / factor)];
            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }

        // write padding for scanline to outfile
        for (int l = 0; l < padding; l++)
        {
            fputc(0x00, outptr);
        }
    }

    // close file
    fclose(inptr);
    fclose(outptr);
    return 0;
}