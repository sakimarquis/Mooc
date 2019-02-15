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

class DisjointSets1:
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

        
a = DisjointSets1(10)
a.union(1,3)
a.union(3,4)
a.union(8,9)
print(a._sizes)

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