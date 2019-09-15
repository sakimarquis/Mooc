# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:28:08 2018

@author: Saki
"""

'''
寻找第6个默尼森数

经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且
满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，
5和31都是素数，因此31是默尼森数。
'''

def isprime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    else:
        return True
        

def monisen(n):
    p = 1
    count = 0
    while True:
        if isprime(p) and isprime(2**p - 1):
            count += 1
            if count == n:
                return 2**p - 1    
        p += 1

print(monisen(6))
            
    
     