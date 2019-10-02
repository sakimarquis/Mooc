# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:33:44 2019

@author: saki
"""
from scipy import stats

# =============================================================================
# 1
# =============================================================================

x1 = 5.667
x2 = 5.830
x3 = 5.978
x4 = 2.69


s1 = stats.norm(loc = 5, scale = 0.5)
s2 = stats.norm(loc = 7, scale = 1)

#def llcdf(x):
#    p_s1_wrong = 1 - s1.cdf(x)
#    p_s2_wrong = s2.cdf(x)
#    return (p_s1_wrong * 2) / (p_s2_wrong * 1)

def ll(x):
    p_s1_wrong = s1.pdf(x)
    p_s2_wrong = s2.pdf(x)
    return (p_s1_wrong * 2) / (p_s2_wrong * 1)


print(ll(x1))
print(ll(x2))
print(ll(x3))
print(ll(x4))


# =============================================================================
# 2
# =============================================================================

prior = 1 / 100000000
p_pos_true = 0.99
p_pos_false = 0.02
p_pos = prior * p_pos_true + (1 - prior) * p_pos_false
p_true = prior

ML = p_pos_true
MAP =  p_pos_true * p_true / p_pos
print(ML)
print(MAP)

