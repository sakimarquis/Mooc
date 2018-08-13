# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 20:14:34 2018

@author: Saki
"""

"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import math
import time

# Desktop imports
import matplotlib.pyplot as plt


############################################
# Provided code

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
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    (cut off the node has most children)
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []
    # O(n)
    while len(new_graph) > 0:
        max_degree = -1
        # O(n)
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        # O(m/n)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


# =============================================================================
# Provided code for application portion of module 2
# 
# Helper class for implementing efficient version
# of UPA algorithm
# =============================================================================

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

##########################################################
# distribution
##########################################################       
    
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

def compute_in_degrees(graph):
    """
    Takes a directed graph digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph. The
    function should return a dictionary with the same set of keys 
    (nodes) as digraph whose corresponding values are the number 
    of edges whose head matches a particular node.
    """
    digraph = copy_graph(graph)
    
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

# =============================================================================
# bfs and compute_resilience
# =============================================================================

from collections import deque

def bfs_visited(ugraph,start_node):
    """
    Takes undirected graph and the start_node 
    and returns the set of all nodes that are 
    visited by a breadth-first search
    """
    graph = copy_graph(ugraph)
    
    visited = set()
    queue = deque([])
    queue.append(start_node)
    
    while len(queue) > 0:
        parent = queue.pop()
        if len(graph[parent]) == 0 and parent not in visited:
            visited.add(parent)
            queue.append(parent)
        for child in graph[parent]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return visited

def cc_visited(ugraph):
    """
    Takes undirected graph and returns a list
    of sets, where each set consists of all 
    the nodes in a connected component
    """
    graph = copy_graph(ugraph)
    remain_nodes = set(graph.keys())
    connected_components = []
    while len(remain_nodes) != 0:    
        start_node = list(remain_nodes)[0]
        connected_component = bfs_visited(graph, start_node)
        connected_components.append(connected_component)
        remain_nodes.difference_update(connected_component)
    return connected_components
        
def largest_cc_size(ugraph):
    """
    Takes undirected graph and returns the size
    of the largest connected component in ugraph.
    """
    graph = copy_graph(ugraph)
    
    largest = 0
    for ele in cc_visited(graph):
        if len(ele) > largest:
            largest = len(ele)
    return largest
    
def compute_resilience(ugraph,attack_order):
    """
    Takes undirected graph. For each node removes the given node 
    and its edges from graph and computes the size of the largest 
    connected component for the resulting graph. 

    return a list (k + 1)th entry is the size of the largest 
    connected component in the graph after removal of the first k 
    nodes in attack_order.First is the largest connected component 
    in the original graph.
    """
    graph = copy_graph(ugraph)
    largest = [largest_cc_size(graph)]
    for node in attack_order:
        graph.pop(node,"No node")
        for key, value in graph.items():
            value.discard(node)
            graph[key] = value
        largest.append(largest_cc_size(graph))
    return largest

# =============================================================================
# make graph
# =============================================================================

def make_ergraph(num_nodes, prob):
    """
    creating undirected ER graphs
    """
    nodes = list(range(num_nodes))
    assert prob <= 1 and prob >= 0 and num_nodes >= 0
    er_graph = {}
    # build nodes
    for node in nodes:
        er_graph[node] = set([])
        
    # count edges
    edges=[]  
    for i in nodes:
        for j in nodes[i+1:]:
            edges.append(tuple([i,j]))
            
    # use ER_algo to add edges
    for edge in edges:
        if prob > random.random():
            er_graph[edge[0]] = er_graph[edge[0]].union([edge[1]])
            er_graph[edge[1]] = er_graph[edge[1]].union([edge[0]])
    return er_graph


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
            dpa_graph[node] = dpa_graph[node].union([new_node])
    return dpa_graph


def random_order(graph):
    """
    takes a graph and returns a list of the nodes in 
    the graph in some random order. 
    """
    random_order = []
    graph_copy = copy_graph(graph)
    for dummy_node in graph:
        node = random.choice(list(graph_copy))
        random_order.append(node)
        graph_copy.pop(node)
    return random_order

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


NODES = 1239.0
EDGES = 3047.0
prob = EDGES / (NODES * (NODES - 1) / 2)
n = int(NODES)
m = int(math.ceil(EDGES / NODES))


network = load_graph(NETWORK_URL)
ER = make_ergraph(n, prob)
UPA = make_upa(n, m)

attack_order = random_order(network)
network_resil = compute_resilience(network,attack_order)
ER_resil = compute_resilience(ER,attack_order)
UPA_resil = compute_resilience(UPA,attack_order)

def q1_plot():
    """
    Plot the answer!!!!
    """
    plt.title("Resilience of graph under random attack")
    plt.xlabel("number of nodes removed")
    plt.ylabel("size of the largest cc")
    plt.plot(network_resil, '-b', label='Computer')
    plt.plot(ER_resil, '-r', label='ER Graph, p = 0.00397')
    plt.plot(UPA_resil, '-g', label='UPA Graph, m = 3')
    plt.legend(loc='upper right')
    plt.show()

def fast_targeted_order(ugraph):
    # copy the graph
    # graph = copy_graph(ugraph)
    
    graph = copy_graph(ugraph)
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


network_attack_order = targeted_order(network)
ER_attack_order = targeted_order(ER)
UPA_attack_order = targeted_order(UPA)

targ_network_resil = compute_resilience(network,network_attack_order)
targ_ER_resil = compute_resilience(ER,ER_attack_order)
targ_UPA_resil = compute_resilience(UPA,UPA_attack_order)

def q4_plot():
    """
    Plot the answer!!!!
    """
    plt.title("Resilience of graph under targeted attack")
    plt.xlabel("number of nodes removed")
    plt.ylabel("size of the largest cc")
    plt.plot(targ_network_resil, '-b', label='Computer')
    plt.plot(targ_ER_resil, '-r', label='ER Graph, p = 0.00397')
    plt.plot(targ_UPA_resil, '-g', label='UPA Graph, m = 3')
    plt.legend(loc='upper right')
    plt.show()

        



