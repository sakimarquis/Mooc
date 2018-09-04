# Questions

## What's `stdint.h`?

a kind of standard type definitions.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

help ensure code portability across platforms and compilers

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

`BYTE`:1
`DWORD`:4
`LONG`:4
`WORD`:2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of 
## any BMP file be? Leading bytes used to identify file formats (with h
## igh probability) are generally called "magic numbers."

BM

## What's the difference between `bfSize` and `biSize`?

'bfSize' is the size of the full bitmap file.
'biSize' is the general information regarding the file.

## What does it mean if `biHeight` is negative?

The bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

3

## Why is the third argument to `fread` always `1` in our code?

the number of data

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

set the pointer

## What is `SEEK_CUR`?

The parameter of the function "fseek",which means current location.
