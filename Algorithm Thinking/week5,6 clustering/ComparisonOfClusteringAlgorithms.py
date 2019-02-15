# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:04:06 2018

@author: Saki
"""
import random
import alg_cluster
import ClosestPairsAndClusteringAlgorithms as fun
import matplotlib.pyplot as plt
import alg_project3_viz as viz
import time

# =============================================================================
# A3Q1
# =============================================================================
def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list 
    corresponds to one randomly generated point in the square 
    with corners (±1,±1). 
    """
    return [alg_cluster.Cluster(set(), random.random()*2-1 , random.random()*2-1, 0, 0) 
            for _ in range(num_clusters)]
    
def a3q1_time():
    num_list = []
    slow = []
    fast = []
    for num in range(2,201):
        num_list.append(num)
        
        clusters = gen_random_clusters(num)
        time1 = time.time()
        fun.slow_closest_pair(clusters)
        time2 = time.time()
        slow.append(time2 - time1)
                
        time1 = time.time()
        fun.fast_closest_pair(clusters)
        time2 = time.time()
        fast.append(time2 - time1)
        
    return [num_list, slow, fast]    


def a3q3_plot(x, y1, y2):
    """
    Plot an example with two curves with legends
    """
    plt.title("Comparing running times of slow/fast closest pair")
    plt.xlabel("number of initial clusters")
    plt.ylabel("running time of the function in seconds")
    plt.plot(x, y1, '-b', label='slow_closest_pair')
    plt.plot(x, y2, '-r', label='fast_closest_pair')
    plt.legend(loc='upper left')
    plt.show()
    
#fun_time = a3q1_time()    
#a3q3_plot(fun_time[0], fun_time[1], fun_time[2]) 


# =============================================================================
# A3Q7
# =============================================================================

def compute_distortion(cluster_list):
    """
    takes a list of clusters and uses
    cluster_error to compute its distortion
    """
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)      
    return distortion


def distortion(data_table, clusters):
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))    
    
    # kmean first for hierarchical_cluster mutate the list
    kmean_cluster = fun.kmeans_clustering(singleton_list, clusters, 5)
    kmean_distortion = compute_distortion(kmean_cluster)
    
    hierarchical_cluster = fun.hierarchical_clustering(singleton_list, clusters)
    hierarchical_distortion = compute_distortion(hierarchical_cluster)    
    
    return (hierarchical_distortion,kmean_distortion)

#test_data_table = viz.load_data_table(viz.DATA_290_URL)
#test_clusters = 16
#    
#data_table = viz.load_data_table(viz.DATA_111_URL)
#clusters = 9
#ans = distortion(data_table, clusters)
 
# =============================================================================
# A3Q10    
# =============================================================================

def a3q10_distortion(data_table):
    num_clusters = range(6,21)
    kmean_distortion = []
    hierarchical_distortion = []
    for num in num_clusters:
        kmean_distortion.append(distortion(data_table, num)[0])
        hierarchical_distortion.append(distortion(data_table, num)[1])
    return (hierarchical_distortion, kmean_distortion)

def a3q10_plot(x, y1, y2, data):
    """
    Plot an example with two curves with legends
    """
    plt.title("Distortion of Hierarchical/KMeans of "+ str(data) + " data")
    plt.xlabel("number of initial clusters")
    plt.ylabel("distortion")
    plt.plot(x, y1, '-b', label='Hierarchical clustering')
    plt.plot(x, y2, '-r', label='KMeans clustering')
    plt.legend(loc='upper right')
    plt.show() 

data = 896
data_table = viz.load_data_table(viz.DATA_896_URL)
x = list(range(6,21))
y1 = a3q10_distortion(data_table)[0]
y2 = a3q10_distortion(data_table)[1]
a3q10_plot(x, y1, y2, data)
       