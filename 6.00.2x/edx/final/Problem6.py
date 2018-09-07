# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:08:45 2018

@author: Saki
"""
 
# =============================================================================
# Problem 6
# =============================================================================

def find_best_combination(choices, total):
    """
    NOT WORK!!!
    
    output:
        list of value in choice best combine to the total
    """
    sort_choices = choices[::]
    sort_choices.sort(reverse = True)
    if total % sort_choices[0] == 0:
        return [sort_choices[0]] * int(total / sort_choices[0])
    elif sort_choices[0] > total:
        return find_combination(sort_choices[1:], total)
    else:
        return [sort_choices[0]] + find_combination(sort_choices[1:], total - sort_choices[0])
           
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools as iter

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    
    LETS BRUTE FORCE!
    """
    results = []
    min_product_sum = float("inf")
    closest = None
    length = len(choices)
    for combination in iter.product(range(2), repeat=length):
        product_sum = sum(np.array(combination) * np.array(choices))
        if product_sum == total:
            results.append(combination)
        elif total > product_sum and (total - product_sum) < min_product_sum:
            min_product_sum = total - product_sum
            closest = combination
        
    if len(results) == 0:
        result = closest
    else:
        min_value = float("inf")
        result = None
        for i in results:
            if sum(i) < min_value:
                min_value = sum(i)
                result = i
            
    return np.array(result)
    

#print(find_combination([1,2,2,3], 4))   
#print(find_combination([1,2,2,3], 12))
#print(find_combination([1,1,3,5,3], 5))
#print(find_combination([1,1,1,9], 4))