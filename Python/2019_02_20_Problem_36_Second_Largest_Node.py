#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 20th
# 
# Problem: Given the root to a binary search tree, find the second largest node in the tree.

# In[3]:


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# In[30]:


def second_largest_node(root):
    def flatten(node):                         # Sub-function to flat out the values in the tree
        values = []                            # A values holder
        if node:                               # If the node exist
            values.append(node.val)            # Put the value in first
            values.extend(flatten(node.left))  # Then examine the left branch
            values.extend(flatten(node.right)) # Then the right branch and add those to the holder
        return values                          # Return the holder
    
    flat_tree = flatten(root)                  # Completely flatten
    
    second_largest = max(filter(lambda x: x != max(flat_tree), flat_tree)) # Simply take the second largest
    
    # Done
    return second_largest


# In[28]:


a = Node(4, Node(6, Node(1), Node(7, Node(2, Node(2)), Node(3))), Node(9, Node(8), Node(5)))


# In[75]:


print('Given the tree below:')
print('         4\n       /   \\\n      6      9\n     / \\    / \\\n    1   7  8   5\n   /\n  2\n / \\\n2   3')
print('The second largest node is {}'.format(second_largest_node(a)))

