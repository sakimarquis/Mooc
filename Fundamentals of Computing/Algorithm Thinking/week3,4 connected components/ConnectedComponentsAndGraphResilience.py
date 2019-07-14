# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:28:23 2018

@author: Saki
"""

from collections import deque

def bfs_visited(ugraph,start_node):
    """
    Takes undirected graph and the start_node 
    and returns the set of all nodes that are 
    visited by a breadth-first search
    """
    visited = set()
    queue = deque([])
    queue.append(start_node)
    
    while len(queue) > 0:
        parent = queue.pop()
        if len(ugraph[parent]) == 0 and parent not in visited:
            visited.add(parent)
            queue.append(parent)
        for child in ugraph[parent]:
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
    remain_nodes = set(ugraph.keys())
    connected_components = []
    while len(remain_nodes) != 0:    
        start_node = list(remain_nodes)[0]
        connected_component = bfs_visited(ugraph, start_node)
        connected_components.append(connected_component)
        remain_nodes.difference_update(connected_component)
    return connected_components
        
def largest_cc_size(ugraph):
    """
    Takes undirected graph and returns the size
    of the largest connected component in ugraph.
    """
    largest = 0
    for ele in cc_visited(ugraph):
        if len(ele) > largest:
            largest = len(ele)
    return largest
    
def compute_resilience(ugraph,attack_order):
    """
    Takes undirected graph, a list of node. For each node 
    in the list, the function removes the given node and 
    its edges from the graph and then computes the size of 
    the largest connected component for the resulting graph. 

    The function should return a list whose (k + 1)th entry 
    is the size of the largest connected component in the 
    graph after the removal of the first k nodes in attack_order.
    The first entry (indexed by zero) is the size of the largest 
    connected component in the original graph.
    """
    largest = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node,"No node")
        for key, value in ugraph.items():
            value.discard(node)
            ugraph[key] = value
        largest.append(largest_cc_size(ugraph))
    return largest


# test
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

attack_order = [1,2,3]
attack_order2 = [4,5,1]
source_node = 0