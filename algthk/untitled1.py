# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:04:28 2018

@author: Saki
"""

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

l = list(range(10))
l = "an"
edge=[]  
for i in l:
    for j in l[i+1:]:
        edge.append(tuple([i,j]))
print edge
        
        