# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import matplotlib.pyplot as plt


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

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

citation_graph = load_graph(CITATION_URL)
indegree_dis = in_degree_distribution(citation_graph)
normalized_dis = normalize_distribution(indegree_dis)

plt.loglog(normalized_dis.keys(), normalized_dis.values(), 'ro')
plt.title('loglog')
plt.xlabel("Citations")
plt.ylabel("Fractions of papers")
plt.show()

indegree_dis = in_degree_distribution(citation_graph)
edge = 0
for key, value in indegree_dis.items():
    edge = edge + key * value 
print edge
print edge / 27770.0









