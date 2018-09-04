# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:49:17 2018

@author: Saki
"""

# =============================================================================
# Problem 3
# =============================================================================

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    ans = []
    check = 0
    s_copy = s
    for i in L:
        multiplier = s_copy // i
        ans.append(multiplier)
        s_copy = s_copy % i
    for idx in range(len(L)):
        check = check + ans[idx] * L[idx]
    if check == s:
        return sum(ans)
    else:
        return "no solution"
    
#print(greedySum([1], 20))
#print(greedySum([10, 5, 1], 14))



# =============================================================================
# Problem 4
# =============================================================================

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    # a O(n^2) implement
    l_copy = L[::]
    l_copy.sort(reverse = True)
    max_val = 0
    for idx in range(len(L)):
        if L[idx] > 0:
            max_now = 0
            for i in L[idx:]:
                max_now += i
                if max_now > max_val:
                    max_val = max_now
    return max_val
         
#def max_contig_sum_n(L):
#    """ a O(n) implement by@anarayanan86"""
#    max_ending_here = max_so_far = L[0]
#    for i in L[1:]:
#        max_ending_here = max(i, max_ending_here + i)
#        max_so_far = max(max_so_far, max_ending_here)
#    return max_so_far

#print(max_contig_sum([3, 4, -1, 5, -4]))
#print(max_contig_sum([3, 4, -8, 15, -1, 2]))
  
# =============================================================================
# Problem 7
# =============================================================================
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    ans_pos = 0
    ans_neg = 0
    while not test(ans_pos) and not test(ans_neg):
        ans_pos += 1
        ans_neg -= 1
    if test(ans_pos):
        return ans_pos
    else:
        return ans_neg

    
# =============================================================================
# #### This test case prints 49 ####
#def f(x):
#    return (x+15)**0.5 + x**0.5 == 15
#print(solveit(f))
# 
# #### This test case prints 0 ####
#def f(x):
#    return x == 0
#print(solveit(f))
# =============================================================================
