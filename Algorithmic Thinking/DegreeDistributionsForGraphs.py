"""
Project #1 - Degree Distributions for Graphs
"""

# Define three constants whose values are dictionaries corresponding to the three directed graphs
EX_GRAPH0 = {0:set([1,2]),
             1:set([]),
             2:set([])}
EX_GRAPH1 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set([])}
EX_GRAPH2 = {0: set([1,4,5]), 
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

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
    
    
    
    
