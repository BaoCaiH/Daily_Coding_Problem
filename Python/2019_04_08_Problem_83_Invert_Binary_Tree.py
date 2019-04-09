#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 8th
# 
# Problem: Invert a binary tree.
# 
# For example, given the following tree:
# 
# `>   a
#    /  \
#   b    c
#  / \   /
# d   e f`
# 
# should become:
# 
# `>    a
#    /   \
#   c     b
#    \   / \
#     f e   d`

# In[1]:


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


# In[2]:


nodeA = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))


# In[4]:


def invertBinaryTree(root):                     #
    if not root:                                # If the node is not available
        return None                             # Return nothing
    node = Node(root.value)                     # Create a node if otherwise
    node.left = invertBinaryTree(root.right)    # And simply reverse the sides
    node.right = invertBinaryTree(root.left)    # Recursively
    return node                                 # Then return the node


# In[5]:


nodeB = invertBinaryTree(nodeA)

