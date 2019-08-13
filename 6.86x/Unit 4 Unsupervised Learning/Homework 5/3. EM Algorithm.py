# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:52:50 2019

@author: saki
"""

import numpy as np
from scipy import stats

weight1 = 0.5
weight2 = 0.5
mu1 = 6
mu2 = 7
sigma1 = 1
sigma2 = 2
x = [-1, 0, 4, 5, 6]

cluster1 = stats.norm(loc = mu1, scale = sigma1)
cluster2 = stats.norm(loc = mu2, scale = sigma2)

# =============================================================================
# Likelihood Function
# =============================================================================

assignment1 = weight1 * cluster1.pdf(x) / (weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x))
assignment2 = weight2 * cluster2.pdf(x) / (weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x))

# this two equations are same, first is from intuition, second is from the problem
log_likelihood = np.sum(np.log(weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x)))
#log_likelihood = np.sum(assignment1 * np.log(weight1 * cluster1.pdf(x) / assignment1) +
#                        assignment2 * np.log(weight2 * cluster2.pdf(x) / assignment2))

# this two equations are not same
#np.sum(np.log(weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x)))
#np.sum(np.log(weight1 * cluster1.pdf(x)) + np.log(weight2 * cluster2.pdf(x)))

# =============================================================================
# E-Step Weights
# =============================================================================

print(assignment2 > assignment1)


# =============================================================================
# M-Step
# =============================================================================

n1 = sum(assignment1)
n2 = sum(assignment2)
new_weight1 = n1 / len(x)
new_weight2 = n2 / len(x)
new_mu1 = sum(assignment1 * x) / n1
new_mu2 = sum(assignment2 * x) / n2
new_sigma1 = sum(assignment1 * (x - new_mu1) ** 2) / n1
new_sigma2 = sum(assignment2 * (x - new_mu2) ** 2) / n2


# =============================================================================
# Training 1,2
# =============================================================================

print(new_mu1 - mu1)
print(new_mu2 - mu2)
print(new_sigma1**2 - sigma1**2)
print(new_sigma2**2 - sigma2**2)


# =============================================================================
# Training 3
# =============================================================================

def EM_one_iteration(x, weight1, weight2, mu1, mu2, sigma1, sigma2):
    cluster1 = stats.norm(loc = mu1, scale = sigma1)
    cluster2 = stats.norm(loc = mu2, scale = sigma2)
    assignment1 = weight1 * cluster1.pdf(x) / (weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x))
    assignment2 = weight2 * cluster2.pdf(x) / (weight1 * cluster1.pdf(x) + weight2 * cluster2.pdf(x))
    n1 = sum(assignment1)
    n2 = sum(assignment2)
    new_weight1 = n1 / len(x)
    new_weight2 = n2 / len(x)
    new_mu1 = sum(assignment1 * x) / n1
    new_mu2 = sum(assignment2 * x) / n2
    new_sigma1 = sum(assignment1 * (x - new_mu1) ** 2) / n1
    new_sigma2 = sum(assignment2 * (x - new_mu2) ** 2) / n2
    return new_weight1, new_weight2, new_mu1, new_mu2, new_sigma1, new_sigma2

for i in range(100):
    new_weight1, new_weight2, new_mu1, new_mu2, new_sigma1, new_sigma2 = EM_one_iteration(x, new_weight1, new_weight2, new_mu1, new_mu2, new_sigma1, new_sigma2)

print(new_weight1, new_weight2)
print(new_mu1, new_mu2)
print(new_sigma1, new_sigma2)
