# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:31:47 2018

@author: Saki
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            # print ("i = %d, j = %d, i >> j = %d" % (i,j,i >> j))
            # 不懂为什么是(i // (3**j) ) % 3 而不是 (i >> j) % 2 == 1
            if (i // (3**j) ) % 3:
                # print ("items = %s" % str(items[j]))
                bag1.append(items[j])
            elif (i // (3**j) ) % 3:
                bag2.append(items[j])
        yield (bag1,bag2)

    
l1 = [1,2]
l = [1,2,3,4,5,6,7]
for i in yieldAllCombos(l):
    print ("combo = %s" % str(i))
