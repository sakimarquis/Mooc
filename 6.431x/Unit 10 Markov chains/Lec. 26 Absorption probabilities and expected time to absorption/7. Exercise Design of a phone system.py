# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:11:40 2018

@author: saki
"""

lamb = 30
Emu = 3
mu = 1/Emu
pi_B = 0.05

pool = 200

def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)

def discrete_approx():
    for B in range(1,pool):
        denominator = 0
        for i in range(B):
            denominator += lamb**i / ((mu**i) * fact(i))
        pi_0 = 1 / denominator
        pi_i = pi_0 * lamb**B / ((mu**B) * fact(B))
        if pi_i <= pi_B:
            return B

print(discrete_approx())