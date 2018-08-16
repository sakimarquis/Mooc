# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:13:45 2018

@author: Saki
"""

import math

# =============================================================================
# Cluster class for Module 3
# =============================================================================

class Cluster:
    """
    Class for creating and merging clusters of counties
    """
    
    def __init__(self, fips_codes, horiz_pos, vert_pos, population, risk):
        """
        Create a cluster based the models a set of counties' data
        """
        self._fips_codes = fips_codes
        self._horiz_center = horiz_pos
        self._vert_center = vert_pos
        self._total_population = population
        self._averaged_risk = risk
        
        
    def __repr__(self):
        """
        String representation assuming the module is "alg_cluster".
        """
        rep = "alg_cluster.Cluster("
        rep += str(self._fips_codes) + ", "
        rep += str(self._horiz_center) + ", "
        rep += str(self._vert_center) + ", "
        rep += str(self._total_population) + ", "
        rep += str(self._averaged_risk) + ")"
        return rep


    def fips_codes(self):
        """
        Get the cluster's set of FIPS codes
        """
        return self._fips_codes
    
    def horiz_center(self):
        """
        Get the averged horizontal center of cluster
        """
        return self._horiz_center
    
    def vert_center(self):
        """
        Get the averaged vertical center of the cluster
        """
        return self._vert_center
    
    def total_population(self):
        """
        Get the total population for the cluster
        """
        return self._total_population
    
    def averaged_risk(self):
        """
        Get the averaged risk for the cluster
        """
        return self._averaged_risk
   
        
    def copy(self):
        """
        Return a copy of a cluster
        """
        copy_cluster = Cluster(set(self._fips_codes), self._horiz_center, self._vert_center,
                               self._total_population, self._averaged_risk)
        return copy_cluster


    def distance(self, other_cluster):
        """
        Compute the Euclidean distance between two clusters
        """
        vert_dist = self._vert_center - other_cluster.vert_center()
        horiz_dist = self._horiz_center - other_cluster.horiz_center()
        return math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
        
    def merge_clusters(self, other_cluster):
        """
        Merge one cluster into another
        The merge uses the relatively populations of each
        cluster in computing a new center and risk
        
        Note that this method mutates self
        """
        if len(other_cluster.fips_codes()) == 0:
            return self
        else:
            self._fips_codes.update(set(other_cluster.fips_codes()))
 
            # compute weights for averaging
            self_weight = float(self._total_population)                        
            other_weight = float(other_cluster.total_population())
            self._total_population = self._total_population + other_cluster.total_population()
            self_weight /= self._total_population
            other_weight /= self._total_population
                    
            # update center and risk using weights
            self._vert_center = self_weight * self._vert_center + other_weight * other_cluster.vert_center()
            self._horiz_center = self_weight * self._horiz_center + other_weight * other_cluster.horiz_center()
            self._averaged_risk = self_weight * self._averaged_risk + other_weight * other_cluster.averaged_risk()
            return self

    def cluster_error(self, data_table):
        """
        Input: data_table is the original table of cancer data used in creating the cluster.
        
        Output: The error as the sum of the square of the distance from each county
        in the cluster to the cluster center (weighted by its population)
        """
        # Build hash table to accelerate error computation
        fips_to_line = {}
        for line_idx in range(len(data_table)):
            line = data_table[line_idx]
            fips_to_line[line[0]] = line_idx
        
        # compute error as weighted squared distance from counties to cluster center
        total_error = 0
        counties = self.fips_codes()
        for county in counties:
            line = data_table[fips_to_line[county]]
            singleton_cluster = Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
            singleton_distance = self.distance(singleton_cluster)
            total_error += (singleton_distance ** 2) * singleton_cluster.total_population()
        return total_error


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
# but received (0.076157731058639044, 0, 1)


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

 
#c1 = Cluster(set([]), 0, 0, 1, 0)
#c2 = Cluster(set([]), 1, 0, 1, 0)
#c3 = Cluster(set([]), 2, 0, 1, 0)
#c4 = Cluster(set([]), 3, 0, 1, 0)
#ans = closest_pair_strip([c1, c2, c3, c4], 1.5, 1.0) 
#expected one of the tuples in set([(1.0, 1, 2)]) but received (1.0, 0, 1)

#c1 = Cluster(set([]), 1.0, 1.0, 1, 0)
#c2 = Cluster(set([]), 1.0, 5.0, 1, 0)
#c3 = Cluster(set([]), 1.0, 4.0, 1, 0)
#c4 = Cluster(set([]), 1.0, 7.0, 1, 0)
#c_list = [c1,c2,c3,c4]
#ans = closest_pair_strip(c_list, 1.0, 3.0) 
#expected one of the tuples in set([(1.0, 1, 2)]) but received (1.0, 2, 1)
    
#c1 = Cluster(set([]), -4.0, 0.0, 1, 0)
#c2 = Cluster(set([]), 0.0, -1.0, 1, 0)
#c3 = Cluster(set([]), 0.0, 1.0, 1, 0) 
#c4 = Cluster(set([]), 4.0, 0.0, 1, 0)
#c_list = [c1,c2,c3,c4]
#ans = closest_pair_strip(c_list, 0.0, 4.1231059999999999) 

#expected one of the tuples in set([(2.0, 1, 2)]) but received (4.1231056256176606, 0, 1)
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    return []


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    return []


