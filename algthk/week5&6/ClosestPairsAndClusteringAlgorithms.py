"""
Created on Thu Aug 16 17:13:45 2018

@author: Saki
"""
import math
import alg_cluster

######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    dist = float("inf")
    closest = tuple([dist, -1, -1])
    
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                if cluster_list[idx1].distance(cluster_list[idx2]) < dist:
                      dist = cluster_list[idx1].distance(cluster_list[idx2])
                      closest = tuple([dist, idx1, idx2])
    return closest

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    if len(cluster_list) <= 3:
        return slow_closest_pair(cluster_list)
    else:
        mid_idx = len(cluster_list)/2
        first = fast_closest_pair(cluster_list[:mid_idx])
        tmp = list(fast_closest_pair(cluster_list[mid_idx:]))
        tmp[1] += mid_idx
        tmp[2] += mid_idx
        last = tuple(tmp)
        closest = first if first[0] <= last[0] else last  
        mid_x = (cluster_list[mid_idx - 1].horiz_center() + cluster_list[mid_idx - 1].horiz_center())/2
        mid =  closest_pair_strip(cluster_list, mid_x, closest[0])
        closest = closest if closest[0] <= mid[0] else mid     
    return closest

#c0 = Cluster(set([]), 0.02, 0.39, 1, 0)
#c1 = Cluster(set([]), 0.19, 0.75, 1, 0)
#c2 = Cluster(set([]), 0.35, 0.03, 1, 0)
#c3 = Cluster(set([]), 0.73, 0.81, 1, 0)
#c4 = Cluster(set([]), 0.76, 0.88, 1, 0)
#c5 = Cluster(set([]), 0.78, 0.11, 1, 0)
#c_list = [c0,c1,c2,c3,c4,c5]
#ans = fast_closest_pair(c_list)

# expected one of the tuples in set([(0.076157731058639044, 3, 4)])


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    index = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width:
            index.append(idx)
    
    dist = float("inf")       
    if len(index) < 2:
        return tuple([dist, -1, -1])
    else:
        index.sort(key = lambda idx: cluster_list[idx].vert_center())

    for idx1 in range(len(index)-1):
        for idx2 in range(idx1+1, min(idx1+3, len(index)-1)+1):
            if cluster_list[index[idx1]].distance(cluster_list[index[idx2]]) < dist:
                  dist = cluster_list[index[idx1]].distance(cluster_list[index[idx2]])
                  closest = tuple([dist, min(index[idx1],index[idx2]), max(index[idx1],index[idx2])])                 
    return closest 

 
#c1 = Cluster(set([]), 0, 3, 3, 0)
#c2 = Cluster(set([]), 1, 2, 2, 1)
#c3 = Cluster(set([]), 2, 1, 1, 2)
#c4 = Cluster(set([]), 3, 0, 0, 3)
#c_list = [c1,c2,c3,c4]
#ans = closest_pair_strip([c1, c2, c3, c4], 1.5, 1.0) 
#expected one of the tuples in set([(1.0, 1, 2)]) 
    
#c1 = Cluster(set([1]), 1.0, 1.0, 1, 0)
#c2 = Cluster(set([2]), 1.0, 5.0, 1, 0)
#c3 = Cluster(set([3]), 1.0, 4.0, 1, 0)
#c4 = Cluster(set([4]), 1.0, 7.0, 1, 0)
#c_list = [c1,c2,c3,c4]
#ans = closest_pair_strip(c_list, 1.0, 3.0) 
#expected one of the tuples in set([(1.0, 1, 2)]) 

#c1 = Cluster(set([]), -4.0, 0.0, 1, 0)
#c2 = Cluster(set([]), 0.0, -1.0, 1, 0)
#c3 = Cluster(set([]), 0.0, 1.0, 1, 0) 
#c4 = Cluster(set([]), 4.0, 0.0, 1, 0)
#c_list = [c1,c2,c3,c4]
#ans = closest_pair_strip(c_list, 0.0, 4.1231059999999999) 
#expected one of the tuples in set([(2.0, 1, 2)]) 

######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        closest = fast_closest_pair(cluster_list)
        cluster_list[closest[1]].merge_clusters(cluster_list[closest[2]])
        cluster_list.remove(cluster_list[closest[2]])
    return cluster_list
    

######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    clusters = cluster_list[::]
    # position initial clusters at the location of clusters with largest populations
    clusters.sort(key = lambda cluster: cluster.total_population(), reverse = True)
    clusters = clusters[:num_clusters]
   
    for _ in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set(),0,0,0,0) for _ in range(num_clusters)]
        for cluster in cluster_list:
            # find closest center
            closest = float("inf")
            for idx in range(len(clusters)):
                dist = clusters[idx].distance(cluster)
                if dist < closest:
                    closest = dist
                    center = idx
            # merge the cluster closest to new_clusters
            new_clusters[center].merge_clusters(cluster)
        # store new center
        clusters = new_clusters
    return clusters


#TEST_CASE= [alg_cluster.Cluster(set(['00']), 0.0, 0.0, 1, 0.1),
#            alg_cluster.Cluster(set(['10']), 1.0, 0.0, 2, 0.1),
#            alg_cluster.Cluster(set(['11']), 1.0, 1.0, 3, 0.1),
#            alg_cluster.Cluster(set(['01']), 0.0, 1.0, 4, 0.1),
#            alg_cluster.Cluster(set(['1010']), 10.0, 10.0, 5, 0.1),
#            alg_cluster.Cluster(set(['1011']), 10.0, 11.0, 6, 0.1),
#            alg_cluster.Cluster(set(['1111']), 11.0, 11.0, 7, 0.1),
#            alg_cluster.Cluster(set(['1110']), 11.0, 10.0, 8, 0.1)]
#
#ans = kmeans_clustering(TEST_CASE, 2, 2)
#(0,0),(0,1),(1,0),(11,) should be in a group
#(10,10),(10,11),(11,10),(11,11) should be in a group