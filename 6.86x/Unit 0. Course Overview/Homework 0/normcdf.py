# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:51:53 2019

@author: saki
"""

from scipy.stats import norm
ans = norm.cdf([0.5,2],loc=1,scale = 2**(1/2))
print(ans[1] - ans[0])