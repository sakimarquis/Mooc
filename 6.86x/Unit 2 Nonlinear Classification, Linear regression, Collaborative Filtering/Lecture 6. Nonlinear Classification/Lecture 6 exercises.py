# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:53:01 2019

@author: saki
"""

import numpy as np
import math

# =============================================================================
# Lecture 5 Exercise 3
# =============================================================================

def multichoose(n,k):
    numerator = math.factorial(n + k - 1)
    denominator = math.factorial(k)*math.factorial(n + k - 1 - k)
    return numerator/denominator

print(multichoose(150,1) + multichoose(150,2) + multichoose(150,3))



