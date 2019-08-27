# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:21:06 2019

@author: saki
"""

# =============================================================================
# 1. Value Iteration for Markov Decision Process
# part b
# =============================================================================

old_b = 0
old_c = 0
old_d = 0
gamma = 0.75
iteration = 10000
for i in range(iteration):
    c = 10 + old_d * gamma
    d = 10 + old_c * gamma
    b = 1 + old_c * gamma
    old_b = b
    old_c = c
    old_d = d
print(b)


# =============================================================================
# 2. Q-Value Iteration
# part 2
# =============================================================================

# states 1, 2, 3; action C
S = [1, 2, 3]
for s in S:
    print(0.7 * 2**(1/3) + 0.3 * (s + 4)**(-1/2))

# states 4, 5, 3; action C
S = [4, 5]
for s in S:
    print((s + 4)**(-1/2))


