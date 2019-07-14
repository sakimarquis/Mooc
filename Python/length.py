# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 00:14:49 2018

@author: Saki
"""

import numpy as np

def length(x):
  """Compute the length of a vector"""
  length_x = (x.T*x)**0.5
  
  return length_x

print(length(np.array([1,1])))