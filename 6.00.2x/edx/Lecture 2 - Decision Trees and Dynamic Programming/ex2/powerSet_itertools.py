# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:37:27 2018

@author: Saki
"""
import itertools

# generate all combinations of N items
def powerSet_itertools(items):
    for j in range(len(l)+1):
        for i in itertools.combinations(l, j):
            yield list(i)
        
l1 = [0,1,2,3]
l = [1,2,3,4,5,6,7]
count = 0
for i in powerSet_itertools(l):
    count += 1
    print (i)
print(count)