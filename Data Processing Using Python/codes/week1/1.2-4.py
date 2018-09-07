# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:21:25 2018

@author: Saki
"""

while True:
    try:
        count = int(input("Enter count: "))
        price = float(input("Enter price for each one: "))
        Pay = count * price
        print("The price is: ", Pay)
        break
    except ValueError:
        print('Error, please enter numeric one. ')
