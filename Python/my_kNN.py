# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:17:08 2019

@author: saki
"""

import numpy as np
import matplotlib.pyplot as plt
from os import listdir


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
# 2.2.1 read data
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
# 2.2.2 plot data
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


# =============================================================================
# 2.2.3 normalizing
# =============================================================================

def mat_norm(matrix):
    """
    input:
        a matrix whose columns are features' value, rows are data
    
    output:
        normalized matrix = ( raw - min )/ range
    """
    min_vals = matrix.min(0)
    max_vals = matrix.max(0)
    ranges = max_vals - min_vals
    col = matrix.shape[0]
    min_tiles = np.tile(min_vals, (col,1))
    ranges_tiles = np.tile(ranges, (col,1))
    normed_mat = (matrix - min_tiles) / ranges_tiles
    return normed_mat, ranges, min_vals
  
normed_mat, ranges, min_vals = mat_norm(features)
print(normed_mat)


# =============================================================================
# 2.2.4 testing date data
# =============================================================================

def date_data(filename = 'datingTestSet2.txt', test_part = 0.1):
    """
    input:
        data filename
    output:
        4 matrix: test_features, test_labels, non_test_features, non_test_labels
        1 number: test_num
    """
    features, labels = file2matrix(filename)
    normed_mat, ranges, min_vals = mat_norm(features)
    
    data_num = normed_mat.shape[0]
    test_num = int(test_part * data_num)
    perm = np.random.permutation(data_num)
    
    test = perm[0:test_num]
    non_test = perm[test_num:]
    test_features = normed_mat[test]
    test_labels = labels[test]
    non_test_features = normed_mat[non_test]
    non_test_labels = labels[non_test]    
    return test_features, test_labels, non_test_features, non_test_labels, test_num

def test_kNN(test_features, test_labels, non_test_features, non_test_labels, test_num, k = 3):
    """
    input:
        4 matrix: test_features, test_labels, non_test_features, non_test_labels
    output:
        error
    """    
    error = 0  
    for i in range(test_num):
        kNN_pred = kNN(test_features[i], non_test_features, non_test_labels, k)
        error = error + 1 - (kNN_pred == test_labels[i])
    return error/normed_mat.shape[0]

test_features, test_labels, non_test_features, non_test_labels, test_num = date_data()
print(test_kNN(test_features, test_labels, non_test_features, non_test_labels, test_num))


# =============================================================================
# 2.2.5 online predict
# =============================================================================

def online_kNN(k = 3):
    result = ['not at all', 'in samll doses', 'in large doses']
    game_time = float(input('percentage of time spent playing video games?'))
    flight_miles = float(input('frequent flier miles earned per year?'))
    icecream = float(input('liters of icecream consumed per year?'))
    
    features, labels = file2matrix('datingTestSet2.txt')
    normed_mat, ranges, min_vals = mat_norm(features)
    
    feature_vec = np.array([game_time, flight_miles, icecream])
    kNN_pred = int(kNN(feature_vec, normed_mat, labels, k))
    
    print("You will probably like this person:",result[kNN_pred - 1])
    
    
# =============================================================================
# 2.3 handwriting recognition
# 2.3.1 transform image to vector
# ============================================================================

def img2vector(filename, row = 32, col = 32):
    img_mat = np.zeros([col, row])
    img = open(filename)
    for i in range(row):
        line = img.readline()
        img_mat[i,:] = np.array([number for number in line][:col])
    return img_mat.reshape(col * row)

# =============================================================================
# 2.3.2 test handwriting recognition
# =============================================================================


def digit_data(folder, test_part = 0.1, row = 32, col = 32):
    """
    input:
        str: folder name
    output:
        4 matrix: test_features, test_labels, non_test_features, non_test_labels
        1 number: test_num
    """
    train_files = listdir(folder)
    data_num = len(train_files)
    features = np.zeros([data_num, col * row])
    labels = []
    for i in range(data_num):
        file_name = train_files[i]
        label = int(file_name.split('_')[0])
        labels.append(label)
        features[i,:] = img2vector(f"{folder}/{file_name}") 
    labels = np.array(labels)
    return features, labels, data_num
    
non_test_features, non_test_labels, data_num = digit_data('trainingDigits')
test_features, test_labels, test_num = digit_data('testDigits')
print(test_kNN(test_features, test_labels, non_test_features, non_test_labels, test_num))