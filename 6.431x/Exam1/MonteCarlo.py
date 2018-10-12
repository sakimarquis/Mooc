# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:33:40 2018

@author: saki
"""
import numpy as np

def simu1():
    N = []
    for i in range(1000):  
        l = [1,1]
        for j in range(3):
            x = np.random.choice([0,1])
            l.append(x)
        N.append(l.count(1))
    return np.var(N, ddof=1)

def simu2():
    N = []
    for i in range(1000):  
        l = []
        for j in range(5):
            x = np.random.choice([0,1])
            l.append(x)
        N.append(l.count(1))
    return np.var(N, ddof=1)

def simu(n):
    vars = []
    for i in range(n):
        vars.append(simu1())
    return np.mean(vars)
        
        
print(simu(1000))
    