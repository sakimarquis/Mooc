# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:29:50 2019

@author: saki
"""

import numpy as np


# =============================================================================
# Lecture 5 Exercise 4
# =============================================================================

def empirical_risk(feature_matrix, labels, theta, theta_0, loss_func):
    agreement = labels - (feature_matrix @ theta + theta_0)
    loss = loss_func(agreement)
    return np.mean(loss)

def hinge_loss(agreement):
    return np.maximum(0, 1 - agreement)

def squared_error_loss(agreement):
    return agreement**2/2

x = np.array([[1,0,1],[1,1,1],[1,1,-1],[-1,1,1]])
y = np.array([2, 2.7, -0.7, 2]).reshape(4,1)
theta = np.array([0, 1, 2]).reshape(3,1)

print(empirical_risk(x, y, theta, 0, hinge_loss))
print(empirical_risk(x, y, theta, 0, squared_error_loss))


