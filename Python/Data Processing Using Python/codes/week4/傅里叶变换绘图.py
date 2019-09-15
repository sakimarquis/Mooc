# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:09:57 2018

@author: Saki
"""

import scipy as sp
import pylab as pl
list1 = sp.ones(500)
list1[100:300]= -1
pl.plot(list1)
f=sp.fft(list1)
pl.plot(f)