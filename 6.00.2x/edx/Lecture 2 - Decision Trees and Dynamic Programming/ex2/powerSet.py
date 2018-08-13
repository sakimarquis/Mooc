# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:12:31 2018

@author: Saki
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            # print ("i = %d, j = %d, i >> j = %d" % (i,j,i >> j))
            if (i >> j) % 2 == 1:
                # print ("items = %s" % str(items[j]))
                combo.append(items[j])
        yield combo
        
l1 = [1,2,3]
l = [1,2,3,4,5,6,7]
count = 0
for i in powerSet(l):
    print ("combo = %s" % str(i))
    count += 1
print (count)