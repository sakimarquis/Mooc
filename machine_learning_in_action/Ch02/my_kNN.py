# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:17:08 2019

@author: saki
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 2.1 KNN
# =============================================================================

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def euclidean_distance(X, data):
    ''' 
    Input: 
        X: 1 vector to compare to existing dataset (1xN)
        data: size m data with N feathers set of known vectors (NxM)
        
    Output:     
        distance between X and all m of Y (NxM)
    '''
    n_data = data.shape[0]
    X_tiles = np.tile(X, (n_data,1))
    distance = np.sqrt( np.sum((X_tiles - data)**2, axis = 1) )
    return distance


def find_maxnum(a_dict):
    """
    input:
        dict: key, num_value
    output:
        the key with max number value
    """
    max_num = 0
    max_label = None
    for k,v in a_dict.items():
        if v > max_num:
            max_num += 1
            max_label = k
    return max_label


def kNN(X, data, labels, k):
    ''' 
    Input: 
        X: 1 vector with N feathers to compare to existing dataset (1xN)
        data: size m data with N feathers set of known vectors (NxM)
        labels: data set labels (1xM vector)
        k: number of neighbors to use for comparison (should be an odd number)
        
    Output:     
        the most popular class label
    '''
    distance = euclidean_distance(X, data)
    sorted_idx = np.argsort(distance)
    label_count = {}  # store the k data's labels
    for i in range(k):
        label = labels[sorted_idx[i]]
        label_count[label] = label_count.get(label, 0) + 1
    return find_maxnum(label_count)
            

group, labels = createDataSet()
print(kNN([0,0], group, labels, 3))


# =============================================================================
# 2.2 kNN and dating website
#
# read data
# =============================================================================

def file2matrix(filename):
    """
    input:
        a text file [feature1 feature2 feature3 label]
        
    output:
        a feature matrix [feature1 feature2 feature3]
        a label array
    """
    text = open(filename)
    text_lines = text.readlines()
    num_lines = len(text_lines)
    num_per_line = len( text_lines[0].strip().split('\t') )
    data_mat = np.zeros((num_lines, num_per_line))
    for i in range(num_lines):
        data_mat[i] = np.array( text_lines[i].strip().split('\t') )
    return data_mat[:, 0:-1],  data_mat[:, -1]

features, labels = file2matrix('datingTestSet2.txt')

# =============================================================================
# plot data
# =============================================================================

# pyploy way

#fig, ax = plt.subplots()
#ax.scatter(features[:,1], features[:,2], 15*labels, labels)
#plt.show()
#fig, ax = plt.subplots()
#ax.scatter(features[:,0], features[:,1], 15*labels, labels)
#plt.show()
#fig, ax = plt.subplots()
#ax.scatter(features[:,0], features[:,2], 15*labels, labels)
#plt.show()

# oops way
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.scatter(features[:,1], features[:,2], 15*labels, labels)
ax2 = fig.add_subplot(312)
ax2.scatter(features[:,0], features[:,1], 10*labels, labels)
ax3 = fig.add_subplot(313)
ax3.scatter(features[:,0], features[:,2], 15*labels, labels)






