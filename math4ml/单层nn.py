# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# First set up the network.
import numpy as np

sigma = np.tanh
w = np.array([[-2, 4, -1],[6, 0, -3]])
b = np.array([0.1, -2.5])

# Define our input vector
x = np.array([0.3, 0.4, 0.1])

# Then we define the neuron activation.
def a1(a0):
    return sigma(w @ a0 + b)
print(w @ x + b)
print(a1(x))

# Calculate the values by hand,
# and replace a1_0 and a1_1 here (to 2 decimal places)
#a1 = np.array([a1_0, a1_1])

