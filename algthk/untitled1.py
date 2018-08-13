# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:04:28 2018

@author: Saki
"""
# =============================================================================
# Provided code for application portion of module 2
# 
# Helper class for implementing efficient version
# of UPA algorithm
# =============================================================================
import random
import matplotlib.pyplot as plt
import time
import math


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def make_upa(n, m):
    """
    creating undirected PA graphs
    """
    dpa_graph = make_complete_graph(m)
    
    obj = UPATrial(m-1)
    for idx in range(m,n):
        new_node = obj._num_nodes
        to_connect = obj.run_trial(m)
        dpa_graph[new_node] = to_connect
        for node in to_connect:
            dpa_graph[node].update([new_node])
    return dpa_graph

# =============================================================================
# helper function
# =============================================================================
def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

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

# =============================================================================
# function to compare time 
# =============================================================================

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order

def fast_targeted_order(ugraph):
    # copy the graph
    # graph = copy_graph(ugraph)
    
    graph = ugraph
    # O(n)
    degree_sets = [set() for idx in range(len(graph))]
    # O(n) kth element is the set of nodes of degree k
    for node in graph:
        degree_sets[len(graph[node])].add(node)
    targeted_order = []
    # iterates degree_sets descendingly
    # O(1) for complete graph, 
    for degree in range(len(graph))[::-1]:
        while len(degree_sets[degree]):
            # chooses node from first set,deletes that node 
            # from graph, updates degree_sets
            max_deg_node = degree_sets[degree].pop()
            # O(n/2) for complete graph,
            for neighbor in graph[max_deg_node]:
                neighbor_deg = len(graph[neighbor])
                degree_sets[neighbor_deg].discard(neighbor)
                degree_sets[neighbor_deg - 1].add(neighbor)
            targeted_order.append(max_deg_node)
            # O(n) or O(2*edges)
            delete_node(graph, max_deg_node) 
    return targeted_order

# =============================================================================
# time it!
# =============================================================================
n_list = list(range(10,1000,10))
m = 5
def time_q3(n_list,m):
    targeted = []
    fast_targeted = []
    for n in n_list:
        upa = make_upa(n, m)

        time1 = time.time()
        targeted_order(upa)
        time2 = time.time()
        targeted.append(time2 - time1)
        
        
        time1 = time.time()
        fast_targeted_order(upa)
        time2 = time.time()
        targeted.append(time2 - time1)
        
    return tuple(targeted, fast_targeted)
        

# =============================================================================
# plot
# =============================================================================



def legend_example():
    """
    Plot an example with two curves with legends
    """
    xvals = [1, 2, 3, 4, 5]
    yvals1 = [1, 2, 3, 4, 5]
    yvals2 = [1, 4, 9, 16, 25]

    plt.plot(xvals, yvals1, '-b', label='linear')
    plt.plot(xvals, yvals2, '-r', label='quadratic')
    plt.legend(loc='upper right')
    plt.show()


def q1_plot():
    """
    Plot an example with two curves with legends
    """
    plt.title("Resilience of graph under random attack")
    plt.xlabel("number of nodes removed")
    plt.ylabel("size of the largest cc")
    plt.plot(network_resil, '-b', label='Computer')
    plt.plot(ER_resil, '-r', label='ER Graph, p = 0.00397')
    plt.plot( UPA_resil, '-g', label='UPA Graph, m = 3')
    plt.legend(loc='upper right')
    plt.show()
    

ugraph = {0:set([1,4,5]),
          1:set([0,2,6]),
          2:set([1,3]),
          3:set([2]),
          4:set([0]),
          5:set([0,6]),
          6:set([1,5]),
          7:set([]),
          8:set([9]),
          9:set([8])}    


        
        