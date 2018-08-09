# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:28:23 2018

@author: Saki
"""
class DisjointSets:
    def __init__(self, nodes):
        self._parents = {}
        self._ranks = {}
        for node in range(nodes):
            self._parents[node] = node
            self._ranks[node] = 0
    
    def find(self, node):
        if node != self._parents[node]:
            # compress the path
            self._parents[node] = self._parents[self._parents[node]]
        return self._parents[node]        

    def union(self, x_set, y_set):
        x_root = self.find(x_set) 
        y_root = self.find(y_set)
        if self._ranks[x_root] > self._ranks[y_root]:
            self._parents[y_root] = x_root
        elif self._ranks[x_root] < self._ranks[y_root]:
            self._parents[x_root] = y_root
        elif self._ranks[x_root] == self._ranks[y_root]:        
            self._parents[y_root] = x_root
            self._ranks[x_root] += 1
                
    
def compute_resilience_uf(ugraph, attack_order):
    """
    use union find to compute resilience
    """
    largest = []
    build_order = []
    
    for node in ugraph.keys():
        if node not in attack_order:
            build_order.append(node)
    build_order = build_order + attack_order[::-1]
    
    disjointset = DisjointSets(len(ugraph))
    built = []
    for node in build_order:
        built.append(node)
        for neighbor in ugraph[node]:
            if neighbor in built:
                disjointset.union(node, neighbor) 
        roots = []
        max_cc = 0
        for node in ugraph:
            roots.append(disjointset.find(node))
        for root in set(roots):
            if roots.count(root) > max_cc:
                max_cc = roots.count(root)
        largest.append(max_cc)
       
        print(roots)
    print (build_order)
    return largest[::-1][:len(attack_order)+1]

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
#source_node = 0