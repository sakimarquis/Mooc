# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:25:20 2019

@author: saki
"""

from scipy.stats import chisquare

n = 275
data = [205,26,25,19]
exp = [0.72,0.07,0.12,0.09]

exp_freq = [n*i for i in exp]
T_n = chisquare(data,exp_freq)
print(T_n)