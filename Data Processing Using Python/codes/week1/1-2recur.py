# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
def fun(num):
    if num<0:  #转换成正数
        print '-',
        num = -num
    if num/10: #不断除以10直到为个位数
        fun(num/10)
    print chr(num%10+48)
  
num=-1234     
print fun(num)
