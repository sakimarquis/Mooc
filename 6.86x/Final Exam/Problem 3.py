# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:56:15 2019

@author: saki
"""
import numpy as np
import matplotlib.pyplot as plt

def Relu(vector):
    return np.maximum(0, vector)


u_a = np.array([1, 1]).reshape(2,1)
u_b = np.array([1, -1]).reshape(2,1)
v_1 = np.array([-1, 1]).reshape(2,1)
v_2 = np.array([1, 0]).reshape(2,1)

coords = np.array([u_a, u_b, v_1, v_2])
labels = np.array([-1, -1, -1, -1])
fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1])

z_a1 = u_a + v_1
z_b1 = u_b + v_1
z_a2 = u_a + v_2
z_b2 = u_b + v_2


# =============================================================================
# 3. (1)
# =============================================================================

print(Relu(z_a1))
print(Relu(z_b1))
print(Relu(z_a2))
print(Relu(z_b2))

coords = np.array([Relu(z_a1), Relu(z_b1), Relu(z_a2), Relu(z_b2)])
labels = np.array([-1, -1, -1, -1])
fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1])


# =============================================================================
# 3. (3)
# =============================================================================

W = np.array([1, 1])
W_0 = -1
y_b2 = np.sign(np.dot(W, Relu(z_b2)) + W_0)
print(y_b2)





