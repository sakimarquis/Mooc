# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:54:29 2018

@author: Saki
"""
import numpy as np
from sympy import *

x=Symbol("x")
y=Symbol("y")
mu=Symbol("mu")
sig=Symbol("sig")
f = np.e**(-(x - y*y + x*y))
g = (1/2 * (np.e**y) + (np.e**-y)) + x - 2
k = (1/(sig*(2*np.pi)**(1/2))) * np.e**(-((x - mu)**2)/(2*sig**2))
diff(k,mu)