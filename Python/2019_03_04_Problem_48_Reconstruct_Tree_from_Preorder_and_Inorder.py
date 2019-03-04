#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 4th
# 
# Problem: Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
# 
# For example, given the following preorder traversal:
# 
# [a, b, d, e, c, f, g]
# 
# And the following inorder traversal:
# 
# [d, b, e, a, f, c, g]
# 
# You should return the following tree:
# 
# `>  a
#    / \
#   b   c
#  / \ / \
# d  e f  g`

# In[10]:


# Create class of a binary tree
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# In[7]:


def reconstruct(preorder, inorder):
    if not preorder:                                              # If no value was left or available
        return None                                               # There is no node
    value = preorder[0]                                           # Take the first value in preorder
    index = inorder.index(value)                                  # Find in inorder (to find the local root)
    left = inorder[:index]                                        # Store whatever on the left
    right = inorder[index+1:]                                     # And the right of the local root
    node = Node(value)                                            # Give the local root a node
    node.left = reconstruct([e for e in preorder if e in left],   # Then the left of that root is constructed
                            left)                                 # with new preorder and inorder
    node.right = reconstruct([f for f in preorder if f in right], # Also on the right
                             right)
    
    return node                                                   # Return the final tree


# In[12]:


a = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
b = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
print('This is the preorder: {}'.format(a))
print('This is the inorder: {}'.format(b))


# In[13]:


c = reconstruct(a, b)


# In[14]:


print('This is the left most value of the tree, just to test')
print(c.left.left.val)

