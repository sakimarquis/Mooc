# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 01:28:05 2018

@author: Saki
"""

import matplotlib.pyplot as plt
import random


x = []
y = []
data = []
for i in range(50):
    x.append(i)
    std = 30
    yi = (3*i+2) + random.uniform(-1 * std, std)
    y.append(yi)
    data.append([i,yi])


plt.scatter(x,y)
plt.show()
