# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:15:25 2019

@author: saki
"""

import numpy as np


dataset = np.array([[0, -6], [4, 4], [0, 0], [-5,2]]).astype(float)
k = 2
init_centers = np.array([[-5, 2], [0, -6]]).astype(float)


def distance(X, dataset, norm):
    '''
    Input:
        X: 1 vector to compare to existing dataset (1 x N)
        dataset: size m data with N features set of known vectors (N x M)
        norm: int, Lp norm

    Output:
        distance between X and all m of Y (NxM)
    '''
    num_data = dataset.shape[0]
    X_tiles = np.tile(X, (num_data,1))
    distance = np.sum(abs(X_tiles - dataset) ** norm, axis = 1) ** (1 / norm)
    return distance


def k_medoids(dataset, init_centers, k, norm):
    centers = init_centers.copy()
    members = np.zeros(dataset.shape[0])
    cost_sum = -1
    old_cost_sum = 0
    while old_cost_sum != cost_sum:
        old_cost_sum = cost_sum
        cost_sum = 0

        # step 1: assign data to closest center
        for i_data in range(dataset.shape[0]):
            dist = distance(dataset[i_data], centers, norm)
            members[i_data] = dist.argmin()

        # step 2: find new center
        # get cluster from step 1
        for i_cluster in range(k):
            cluster = dataset[members == i_cluster]
            # find new center minimize the cost for this cluster
            cost = np.ones(cluster.shape[0])
            for i_data in range(cluster.shape[0]):
                cost[i_data] = np.sum(distance(cluster[i_data], cluster, norm))
            centers[i_cluster] = cluster[cost.argmin()]
            cost_sum += cost.min()

    return centers, members


print(k_medoids(dataset, init_centers, k, 1))
print(k_medoids(dataset, init_centers, k, 2))
