# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:55:30 2018

@author: saki
"""
import numpy as np

def gen_dataset(n, d = 2):
    """
    generate a dataset from space X = [−1, 1] × [−1, 1]
    """
    x0 = np.ones((n,1))
    x = np.random.uniform(-1, 1, (n, d))
    return np.hstack([x0, x])

def pla(dataset):
    """
    pla as Perceptron Learning Algorithm
    """
    point1, point2 = np.random.uniform(-1, 1, (2,2))
    interval = point1 - point2
    gradient = interval[1] / interval[0]
    bias = point1[1] - point1[0] * gradient
    #  w0 + w1*x1 + w2*x2 = 0
    target_weight = np.matrix([bias, gradient, -1]).T
    y = np.sign(dataset * target_weight) # wT*x
    # initial the weight
    weight = np.matrix([0.0, 0.0, 0.0]).T
    h = np.sign(dataset * weight) # wT*x
    nums_iter = 0
    while any(h != y):
        misclassified = np.nonzero(h != y) # np.where, np.argwhere
        mis_idx = np.random.choice(misclassified[0])
        weight = (weight.T + y[mis_idx] * dataset[mis_idx]).T
        nums_iter += 1
        h = np.sign(dataset * weight)
    
    NUMS_TEST = 1000
    test_data = gen_dataset(NUMS_TEST, d = 2)
    y_test = np.sign(test_data * target_weight)
    h_test = np.sign(test_data * weight)
    disagreement = np.argwhere(y_test != h_test)
    disagree_prob = len(disagreement) / NUMS_TEST
    return nums_iter, disagree_prob
        
def simu_pla(dataset):
    """
    a simulation of Perceptron Learning Algorithm
    """
    RUNS = 1000
    nums_iter = 0
    disagreement = 0
    for _ in range(RUNS):
        nums_iter += pla(dataset)[0]
        disagreement += pla(dataset)[1]
    return nums_iter/RUNS, disagreement/RUNS