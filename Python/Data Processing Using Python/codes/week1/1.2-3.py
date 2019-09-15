# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:14:50 2018

@author: Saki
"""

'''
验证哥德巴赫猜想之一：2000以内的正偶数（大于等于4）都能够分
解为两个质数之和。每个偶数表达成形如：4=2+2的形式，输出时每
行显示6个式子。
'''

n = [1]
j = 2
x = 2
count = 7

for i in range(2,2000):
    while j <= 2000:
        if i % j == 0:
            break
        else:
            n.append(i)
            i += 1

for y in n:
    for z in n:
        while x <= 2000:
            if x == y + z: 
                if count % 6 == 0:
                    print ("")
                print (("%i + %i = %i") % (y,z,x),end = '  ')
                x += 2
                count += 1
                break
else:
    print ("\n\n2000以内的正偶数（大于等于4）都能够分解为两个质数之和.")
        


            


