# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:42:19 2019

@author: saki
"""

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position <= 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
