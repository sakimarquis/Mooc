# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:52:50 2019

@author: saki
"""
import numpy as np


coords = np.array([[0, 0], [2, 0], [1, 1], [0, 2], [3, 3], [4, 1], [5, 2], \
                   [1, 4], [4, 4], [5, 5]])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
mistakes = np.array([1, 65, 11, 31, 72, 30, 0, 21, 4, 15])

# =============================================================================
# 2. (2)
# =============================================================================

def quadratic_feature(mat):
    quad_mat = np.zeros([10, 3])
    quad_mat[:,0] = mat[:, 0] ** 2
    quad_mat[:,1] = 2**(1/2) * mat[:, 0] * mat[:, 1]
    quad_mat[:,2] = mat[:, 1] ** 2
    return quad_mat

quad_features = quadratic_feature(coords)

theta = np.array([0, 0, 0])
theta0 = 0
theta = theta + np.einsum('ij->j', quad_features * (labels * mistakes).reshape(10, 1))
theta0 = theta0 + labels @ mistakes

# =============================================================================
# 2. (3)
# =============================================================================

def check_theta(theta, theta0, points, labels):
    epsilon = 1e-10
    for i in range(len(coords)):
        if labels[i] * (coords[i] @ theta + theta0) < epsilon:
            print("shit")
            return
    print("Yes! all points are correctly classified")
    print(theta, theta0)

check_theta(theta, theta0, quad_features, labels)