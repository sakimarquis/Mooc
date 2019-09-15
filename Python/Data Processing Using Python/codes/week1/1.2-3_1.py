# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:18:30 2018

@author: Saki
"""

#-*-coding:utf-8-*-
def isPrime(n):
    i = 2
    while i < n // 2 + 1:
        if n % i == 0:
            return False
        i += 1
    return True

m = 4
count = 0
while m < 2000:
    i = 2
    while i < m:
        if isPrime(i) and isPrime(m-i):
            count += 1
            if count % 6 != 0:
                print("{}={}+{}".format(m,i,m-i),end=" ")
            else:
                print("{}={}+{}".format(m,i,m-i))
            m += 2
            break
        else:
            i += 1