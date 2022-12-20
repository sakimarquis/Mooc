# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:49:41 2022
hdx@arizona.edu
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100000
theta1 = np.random.normal(loc=0, scale=np.sqrt(10), size=n)
theta2 = np.random.normal(loc=0, scale=np.sqrt(1), size=n)

x = np.random.normal(loc=theta1, scale=np.sqrt(2), size=n) / 2 + \
    np.random.normal(loc=theta1+theta2, scale=np.sqrt(2), size=n) / 2


plt.hist(x, bins=100, density=True)
# plt.ylim(-10, 10)
# plt.xlim(-10, 10)
