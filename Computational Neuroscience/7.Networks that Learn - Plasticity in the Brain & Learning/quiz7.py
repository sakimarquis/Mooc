# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:29:03 2019

@author: saki
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1
# =============================================================================

Q = np.array([[0.2, 0.1],
              [0.1, 0.15]])

eig_val, eig_vec = np.linalg.eig(Q)


print(eig_vec[:,0])

w = eig_vec[:,0] * -2
print(w)
print(Q @ w)


# =============================================================================
# 7
# =============================================================================

import pickle
with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)

ipt = data['c10p1']
plt.scatter(ipt[:,0], ipt[:,1])

norm_ipt = ipt - ipt.mean()
plt.scatter(norm_ipt[:,0], norm_ipt[:,1])

eta = 1
alpha = 1
delta_t = 0.01
epsilon = 1e-4

w = np.random.random()
for _ in range(1000):
    for u in norm_ipt:
        v = np.dot(u, w)
        w = w + delta_t * eta * (v * u - alpha * v**2 * w)
print(w)

cov_mat = (norm_ipt.T @ norm_ipt) / norm_ipt.shape[0]
eig_val, eig_vec = np.linalg.eig(cov_mat)
print(eig_vec[:,0])













