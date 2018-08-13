# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:36:48 2018

@author: saki
"""

"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import matplotlib.pyplot as plt

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes and returns a dictionary 
    corresponding to a complete directed graph with 
    the specified number of nodes. 
    
    A complete graph contains all possible edges subject to 
    the restriction that self-loops are not allowed. The 
    nodes of the graph should be numbered 0 to num_nodes-1 
    when num_nodes is positive. Otherwise, the function 
    returns a dictionary corresponding to the empty graph.
    """
    if num_nodes <= 1:
        return {0: set([])}
    else:
        graph = {}
        graph_set = set([node for node in range(num_nodes)])
        for node in range(num_nodes):
            tmp = graph_set.copy()
            tmp.discard(node)
            graph[node] = tmp       
        return graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph. The
    function should return a dictionary with the same set of keys 
    (nodes) as digraph whose corresponding values are the number 
    of edges whose head matches a particular node.
    """
    in_degrees = {}
    for key in digraph.keys():
        in_degrees[key] = 0
    for value in digraph.values():
        for node in value:
            in_degrees[node] += 1
    return in_degrees       

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary)
    and computes the unnormalized distribution of the in-degrees
    of the graph. The function should return a dictionary whose 
    keys correspond to in-degrees of nodes in the graph. The value
    associated with each particular in-degree is the number of 
    nodes with that in-degree. In-degrees with no corresponding 
    nodes in the graph are not included in the dictionary.
    """
    in_degree = compute_in_degrees(digraph)
    distribution = {}
    for value in in_degree.values():
        if value in distribution:
            distribution[value] += 1
        else:
            distribution[value] = 1
    return distribution

def normalize_distribution(distribution):
    """
    normalize the distribution
    (make the values in the dictionary sum to one)
    """
    all_dis = 0.0
    ans = {}
    for value in distribution.values():
        all_dis += value
    for key, value in distribution.items():
        ans[key] = value / all_dis
    return ans


n = 27770
m = 13

#n = 20
#m = 5

dpa_graph = make_complete_graph(m)


obj = DPATrial(m-1)
for idx in range(m,n):
    dpa_graph[obj._num_nodes] = obj.run_trial(m)

dpa_indegree = in_degree_distribution(dpa_graph)
dpa_normalized = normalize_distribution(dpa_indegree)
  
plt.loglog(dpa_normalized.keys(), dpa_normalized.values(), 'ro')
plt.title('loglog_DPA')
plt.xlabel("Edges")
plt.ylabel("Nodes")
plt.show()    