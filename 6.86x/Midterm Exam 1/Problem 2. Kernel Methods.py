# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:52:50 2019

@author: saki
"""
import numpy as np
import matplotlib.pyplot as plt


coords = np.array([[0, 0], [2, 0], [1, 1], [0, 2], [3, 3], [4, 1], [5, 2], \
                   [1, 4], [4, 4], [5, 5]])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
mistakes = np.array([1, 65, 11, 31, 72, 30, 0, 21, 4, 15])

fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1], c =labels)

# =============================================================================
# 2. (2), (3)
# =============================================================================

def quadratic_feature(feature):
    quad_mat = np.zeros([10, 3])
    quad_mat[:, 0] = feature[:, 0] ** 2
    quad_mat[:, 1] = np.sqrt(2) * feature[:, 0] * feature[:, 1]
    quad_mat[:, 2] = feature[:, 1] ** 2
    return quad_mat

quad_features = quadratic_feature(coords)

theta = np.array([0, 0, 0])
theta0 = 0
theta = theta + np.einsum('ij->j', quad_features * (labels * mistakes).reshape(10, 1))
theta0 = theta0 + labels @ mistakes

def check_theta(theta, theta0, points, labels):
    epsilon = 1e-10
    for i in range(len(points)):
        if labels[i] * (points[i] @ theta + theta0) < epsilon:
            print("shit")
            return
    print("Yes! all points are correctly classified")
    print(theta, theta0)

check_theta(theta, theta0, quad_features, labels)


fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1], c = labels)
# 21x^2 - 22.627417xy + 22y^2 -110 = 0
x = np.linspace(0, 3, 100)
y = 0.514259 * x - 2.27273 * 10**-8 * np.sqrt(9680000000000000 - 1335999999908111 * x**2)
ax.plot(x, y, linestyle='--')
y = 2.27273 * 10**-8 * (np.sqrt(9680000000000000 - 1335999999908111 * x**2) + 22627417 * x)
ax.plot(x, y, linestyle='--')
