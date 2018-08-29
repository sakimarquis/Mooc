# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:28:28 2018

@author: Saki


Another way to implement PS2, it's false, but i don't know why.

There are other questions confused me.


1,same call: shortest_path = get_best_path(digraph, start, end, [[], 0, 0], 
                                  max_dist_outdoors, None, None, max_total_dist)
# this is right
get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path, max_total_dist = 99999):
# this the compiler tells me needs argument max_total_dist
get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path, max_total_dist):   

# this is right
path = [path[0] + [start], path[1]]
# but this is wrong
path[0] += [start]

# this is right
elif start == end:
    return path[0]
# this is wrong
elif start == end:
    return [start]
    
# why totol_dist != really distance

"""
from graph import Digraph, Node, WeightedEdge

#def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path):
#    start = Node(start)
#    end = Node(end)
#    path = [path[0] + [start], path[1], path[2]]
#    if not (digraph.has_node(start) and digraph.has_node(end)):
#        raise ValueError('Not valid start or end')
#    elif start == end:
#        return path[0]
#    else:
#        for edge in digraph.get_edges_for_node(start):
#            node = edge.get_destination()
#            if node not in path[0]: #avoid cycles
#                print(path)
#                if best_path == None or len(path[0]) < len(best_path):       
#                    new_path = get_best_path(digraph, node, end, path, max_dist_outdoors, best_dist, best_path)
#                    if new_path != None:
#                        best_path = new_path
#    return tuple(best_path)



def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path, max_total_dist = 99999):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    start = Node(start)
    end = Node(end)
    path = [path[0] + [start], path[1], path[2]]
    if not (digraph.has_node(start) and digraph.has_node(end)):
        raise ValueError('Not valid start or end')
    elif start == end:
        return path[0]
    else:
        for edge in digraph.get_edges_for_node(start):
            node = edge.get_destination()
            if node not in path[0]:
                if best_dist == None or path[1] < best_dist:
                    totol_dist = path[1] + int(edge.get_total_distance())
                    outdoor_dist = path[2] + int(edge.get_outdoor_distance())
                    new_path = get_best_path(digraph, node, end, [path[0], totol_dist, outdoor_dist], 
                                             max_dist_outdoors, best_dist, best_path)
                    # why totol_dist != really distance
                    if (new_path != None):
                        if (best_dist == None or outdoor_dist < best_dist) and (outdoor_dist <= max_dist_outdoors) and (totol_dist <= max_total_dist):
                            best_path = new_path
                            best_dist = totol_dist
    return best_path

def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on
# Problem 3c: Implement directed_dfs the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """    
    shortest_path = get_best_path(digraph, start, end, [[], 0, 0], 
                                  max_dist_outdoors, None, None, max_total_dist)
    if shortest_path == None:
        raise ValueError('No path') 
    else:
        return [str(node) for node in shortest_path]   