# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:10:45 2018

@author: Saki
"""

class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # This function is necessary so that Nodes can be used as
        # keys in a dictionary, even though Nodes are mutable
        return self.name.__hash__()


class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, total_distance, outdoor_distance):
        Edge.__init__(self, src, dest)
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance

    def get_total_distance(self):
        return self.total_distance

    def get_outdoor_distance(self):
        return self.outdoor_distance

    def __str__(self):
        # can't figure out why can't pass test_graph_str 
        # display a stange str with or without a space     
        return '{} ({}, {})'.format(Edge.__str__(self),self.total_distance, self.outdoor_distance)
    
        #return Edge.__str__(self)+' ({}, {})'.format(self.total_distance, self.outdoor_distance)       
        #return '{}->{} ({}, {})'.format(self.src, self.dest, self.total_distance, self.outdoor_distance)
        #return str(self.src) + "->"+ str(self.dest) +"("+ str(self.total_distance) + ", " + str(self.outdoor_distance) +")"

class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dict of Node -> list of edges

    def __str__(self):
        edge_strs = []
        print(self.edges)
        print(type(self.edges))
        for edges in self.edges.values():
            for edge in edges:
                edge_strs.append(str(edge))
        edge_strs = sorted(edge_strs)  # sort alphabetically
        return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

    def get_edges_for_node(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def add_edge(self, edge):
        """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the graph."""
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(edge)


def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    print("Loading map from {}.".format(map_filename))
    g = Digraph()
    f = open(map_filename, 'r')
    
    nodes = []
    weighted_edges = []
    for line in f:
        line = line.rstrip()
        line_data = line.split(' ')
        nodes.append(line_data[0])
        nodes.append(line_data[1])
        weighted_edges.append(line_data)
      
    for n in set(nodes):
        node = Node(n)
        g.add_node(node)
       
    for edge in weighted_edges:
        src = Node(edge[0])
        dest = Node(edge[1])
        weighted_edge = WeightedEdge(src, dest, edge[2], edge[3])
        g.add_edge(weighted_edge)
    
    return g   

test = load_map("test_load_map.txt")
print(test)