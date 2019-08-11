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

# 21*x^2 - 22.627417*sqrt(2)*xy + 22*y^2 -110 = 0
# y1 = 0.727273*x - 6.52622*10**-11 * np.sqrt(1173941427012615012352 - 99930551202753069056*x**2)
# y2 = 6.52622*10**-11 *(np.sqrt(1173941427012615012352 - 99930551202753069056 * x**2) + 11143856577*x)
x = np.linspace(0, 3.4, 100)
y1 = 0.727273*x - 6.52622*10**-11 * (1173941427012615012352 - 99930551202753069056*x**2)**(1/2)
y2 = 6.52622*10**-11 * ((1173941427012615012352 - 99930551202753069056 * x**2)**(1/2) + 11143856577*x)
ax.plot(x, y1, linestyle='--')
ax.plot(x, y2, linestyle='--')
