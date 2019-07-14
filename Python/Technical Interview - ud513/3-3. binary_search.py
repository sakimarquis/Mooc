# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:42:21 2019

@author: saki
"""

"""
Python lists have a function called index(), which just does a search and 
returns the first index with an instance of that value. 
"""
l = [3,"saki",3, [2,1], 3]
print(l.index(3))
print(l.index("saki"))
print(l.index([2,1]))
print()

"""
You should use an iterative approach - meaning using loops.

Your function should take two inputs: a Python list to search through, and 
the value you're searching for.

Assume the list only has distinct elements, meaning there are no repeated values, and 
elements are in a strictly increasing order. Return the index of value, or -1 if the value
doesn't exist in the list.
"""

def binary_search(input_array, value):
    input_copy = input_array
    while len(input_copy) > 1:
        half = round(len(input_copy)/2)        
        if input_copy[half] == value:
            return half
        elif input_copy[half] < value:
            input_copy = input_copy[half+1:]
        elif input_copy[half] > value:
            input_copy = input_copy[:half]            
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))