# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:22:47 2018

@author: Saki
"""

'''
验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的
另两个3位数也是37的倍数。（注意验证命题的结果输出方式，只要输出命题
为真还是假即可，而非每一个三位数都有一个真假的输出）
'''

for num in range(100, 1000):
    if num % 37 == 0:
        num_new_1 = num % 100 *10 + num // 100
        num_new_2 = num % 10 * 100 + num // 10
        if num_new_1 % 37 != 0 or num_new_1 % 37 != 0:
            print("It's a false proposition.")
            break
else:
    print("It's a true proposition.")
    