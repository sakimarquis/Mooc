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
edge=[]  
for i in l:
    for j in l[i+1:]:
        edge.append(tuple([i,j]))
#print edge

"""
Short example of creating a legend in matplotlib
"""

import matplotlib.pyplot as plt


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
    


        
        