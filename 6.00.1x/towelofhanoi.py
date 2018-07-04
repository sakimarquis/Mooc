# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print a+'-->'+c
    else:
        move(n-1, a, c, b)     #将前n-1个盘子从A移动到B上
        move(1,a,b,c)           #将最底下的最后一个盘子从A移动到C上
        move(n-1, b, a, c)     #将B上的n-1个盘子移动到C上

print move(7, 'A', 'B', 'C')
