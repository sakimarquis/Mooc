# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 23:47:21 2018

@author: Saki
"""

# =============================================================================
# ex3
# =============================================================================
import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    len_list = []
    for i in L:
        len_list.append(len(i))
    mean = sum(len_list) / len(len_list)
    SS = 0
    for i in len_list:
        SS = SS + (i - mean)**2
    std = math.sqrt(SS/len(len_list))
    return std


#L = ['a', 'z', 'p']
#print(stdDevOfLengths(L))
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
#print(stdDevOfLengths(L))
    
# =============================================================================
# ex4
# =============================================================================
def coefficientOfVariation(L):
    mean = sum(L) / len(L)
    SS = 0
    for i in L:
        SS = SS + (i - mean)**2
    std = math.sqrt(SS/len(L))
    coefficient_of_variation = std / mean
    return coefficient_of_variation

#L = [10, 4, 12, 15, 20, 5] 
#print(coefficientOfVariation(L))
    


