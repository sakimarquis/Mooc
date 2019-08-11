# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:17:24 2019

@author: saki
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC


coords = np.array([[0, 0], [2, 0], [3, 0], [0, 2], [2, 2], [5, 1], [5, 2], \
                   [2, 4], [4, 4], [5, 5]])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
mistakes = np.array([1, 9, 10, 5, 9, 11, 0, 3, 1, 1])


fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1], c =labels)


# =============================================================================
# 1. (1)
# =============================================================================
theta = np.array([0, 0])
theta0 = 0
theta = theta + np.einsum('ij->j', coords * (labels * mistakes).reshape(10, 1))
theta0 = theta0 + labels @ mistakes

def check_theta(theta, theta0, points, labels):
    epsilon = 1e-10
    for i in range(len(coords)):
        if labels[i] * (coords[i] @ theta + theta0) < epsilon:
            print("shit")
            return
    print("Yes! all points are correctly classified")
    print(theta, theta0)


check_theta(theta, theta0, coords, labels)

# 4x + 4y -18 = 0
x = np.linspace(0, 5, 100)
y = (18 - 4 * x) / 4
ax.plot(x, y)

# =============================================================================
# 1. (2)
# =============================================================================

print(np.array([0, 0]) @ np.array([5, 2]) + 0 > 0)

# =============================================================================
# 1. (3)
# =============================================================================

clf = LinearSVC(penalty='l2', C = 1e8, loss='hinge')
clf.fit(coords, labels)
check_theta(clf.coef_.reshape(2), clf.intercept_, coords, labels)


fig, ax = plt.subplots()
ax.scatter(coords[:,0], coords[:,1], c =labels)
# 4x + 4y -18 = 0
y = (18 - 4 * x) / 4
ax.plot(x, y, linestyle='--')
# 0.33559923x + 0.35592746y - 1.50554319 = 0
y1 = (-clf.intercept_[0] - clf.coef_[0][0] * x) / clf.coef_[0][1]
ax.plot(x, y1)


# =============================================================================
# 1. (4)
# =============================================================================

print(1/np.linalg.norm(clf.coef_))

# =============================================================================
# 1. (5)
# =============================================================================

def hinge_loss(points, labels, theta, theta_0):
    agreement = labels * (points @ theta + theta_0)
    hinge_loss = np.maximum(0, 1 - agreement)
    print(np.sum(hinge_loss))


hinge_loss(coords, labels, clf.coef_.reshape(2), clf.intercept_)

# =============================================================================
# 1. (6)
# =============================================================================

hinge_loss(coords, labels, clf.coef_.reshape(2) / 2, clf.intercept_ / 2)

