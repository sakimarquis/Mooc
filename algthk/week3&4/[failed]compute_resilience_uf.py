# -*- coding: utf-8 -*-
"""
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]
    
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:        
            self._parents[pv] = pu
            self._ranks[pu] += 1
        
        return True      

Created on Thu Aug  9 09:50:53 2018

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



class DisjointSets:
    def __init__(self, nodes):
        self._parents = {}
        self._ranks = {}
        self._sizes = {}
        for node in range(nodes):
            self._parents[node] = node
            self._ranks[node] = 0
            self._sizes[node] = 1
    
    def find(self, node):      
        if node != self._parents[node]:
            # compress the path
            self._parents[node] = self._parents[self._parents[node]]
        return self._parents[node]
    
    def union(self, x_set, y_set):
        x_root, y_root = self.find(x_set), self.find(y_set)
        if x_root != y_root:
            if self._ranks[x_root] > self._ranks[y_root]:
                self._parents[y_root] = x_root
                self._sizes[x_root] = self._sizes[x_root] + self._sizes[y_root]
            elif self._ranks[x_root] < self._ranks[y_root]:
                self._parents[x_root] = y_root
                self._sizes[y_root] = self._sizes[x_root] + self._sizes[y_root]
            else:        
                self._parents[y_root] = x_root
                self._sizes[x_root] = self._sizes[x_root] + self._sizes[y_root]
                self._ranks[x_root] += 1

                
#    def union(self, x_set, y_set):
#        x_root, y_root = self.find(x_set), self.find(y_set)
#        if x_root != y_root:
#            if self._sizes[x_root] >= self._sizes[y_root]:
#                self._parents[y_root] = x_root
#                self._sizes[x_root] = self._sizes[x_root] + self._sizes[y_root]
#            else:
#                self._parents[x_root] = y_root
#                self._sizes[y_root] = self._sizes[x_root] + self._sizes[y_root]

                      
 
class DisjointSets1:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [0 for i in range(n + 1)]
        self._sizes = [1 for i in range(n + 1)]
    
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
            self._sizes[pv] += self._sizes[pu]
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
            self._sizes[pu] += self._sizes[pv]
        else:        
            self._parents[pv] = pu
            self._sizes[pu] += self._sizes[pv]
            self._ranks[pu] += 1
        
        return True      

           
        
a = DisjointSets1(10)
a.union(1,3)
a.union(3,4)
a.union(8,9)

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
attack_order2 = [0,1,2,3,4,5,6,7,8,9,10]

def compute_resilience(ugraph, attack_order):
    """
    use union find to compute resilience
    """
    largest = []
    build_order = []
    
    #compute the build order
    for node in ugraph.keys():
        if node not in attack_order:
            build_order.append(node)
            
    build_order = build_order + attack_order[::-1]        
#    for node in attack_order[::-1]:
#        if node in ugraph.keys():
#            build_order.append(node)
    print(build_order)
    #use disjoint set to build the graph
    disjointset = DisjointSets1(len(ugraph))
    built = []
    for node in build_order:
        if node not in ugraph.keys():
            if len(largest) == 0:
                largest.append(0)
            else:
                largest.append(largest[-1])
        else:
            built.append(node)
            for neighbor in ugraph[node]:
                if neighbor in built:
                    disjointset.union(node, neighbor) 
        
        #largest.append(max(disjointset._sizes.values()))
        largest.append(max(disjointset._sizes))
    return largest[::-1][:len(attack_order)+1]