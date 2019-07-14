# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:19:31 2018

@author: Saki
"""
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
import math
import urllib2

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
# 3 graph!
# =============================================================================

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
    
    obj = UPATrial(m)
    for idx in range(m,n):
        new_node = obj._num_nodes
        to_connect = obj.run_trial(m)
        dpa_graph[new_node] = to_connect
        for node in to_connect:
            dpa_graph[node] = dpa_graph[node].union([new_node])
    return dpa_graph

# =============================================================================
# resilience and plot
# =============================================================================
NODES = 1239.0
EDGES = 3047.0
prob = EDGES / (NODES * (NODES - 1) / 2)
n = int(NODES)
m = int(math.ceil(EDGES / NODES))

network = load_graph(NETWORK_URL)
ER = make_ergraph(n, prob)
UPA = make_upa(n, m)

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
    plt.plot(targ_network_resil, '-b', label='Computer network')
    plt.plot(targ_ER_resil, '-r', label='ER Graph, p = 0.00397')
    plt.plot(targ_UPA_resil, '-g', label='UPA Graph, m = 3')
    plt.legend(loc='upper right')
    plt.show()


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




        
        
