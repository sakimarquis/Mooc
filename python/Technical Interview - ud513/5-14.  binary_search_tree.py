# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:08:55 2019

@author: saki
"""

"""
This time, you'll implement search() and insert(). You should rewrite search() 
and not use your code from the last exercise so it takes advantage of BST 
properties. Feel free to make any helper functions you feel like you need, 
including the print_tree() function from earlier for debugging. You can 
assume that two nodes with the same value won't be inserted into the tree. 
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    
    def search_print(self, find_val, traversal = ""):
        return self.search_print_helper(self.root, find_val, "")[:-1]
    
    def insert_helper(self, start, new_val):
        if start.value < new_val:
            if start.right:
               self.insert_helper(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
               self.insert_helper(start.left, new_val)
            else:
                start.left = Node(new_val)  
                
    def search_helper(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.search_helper(start.right, find_val)
            else:
                return self.search_helper(start.left, find_val)
        return False
    
    def search_print_helper(self, start, find_val, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            if start.value < find_val:
                traversal = self.search_print_helper(start.right, find_val, traversal)
            else:
                traversal = self.search_print_helper(start.left, find_val, traversal)
        return traversal
    
 
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
print(tree.search_print(0))