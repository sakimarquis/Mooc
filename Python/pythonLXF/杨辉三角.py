# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:27:27 2018

@author: Saki
"""

def triangles():
    lsstore = [1]
    while True:
        ls = lsstore
        yield ls      
        lsstore = [1]
        for i in range(len(ls)-1):       
            lsstore.append(ls[i]+ls[i+1])      
        lsstore.append(1) 

#ls = [1]
#while True:
#    yield ls
#    ls = [1] + [ls[i] + ls[i+1] for i in range(len(ls)-1) ] + [1] 

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break