#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 5th
# 
# Problem: Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
# 
# `>   a
#    /  \
#   b    c
#  /
# d`

# In[1]:


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


# In[2]:


node_a = Node('a', Node('a', Node('a', Node('a'))), Node('a', Node('a'), Node('a', Node('a', Node('b')), Node('a'))))
node_b = Node('a', Node('b', Node('d')), Node('c'))


# In[3]:


def deepestNode(root):                                              # Main function
    targetDepth = depth(root)                                       # Check the depth of the deepest node
    goLeft = deepPath(root.left, '.left', targetDepth)              # Check the left side
    goRight = deepPath(root.right, '.right', targetDepth)           # Check the right side
    if goLeft:                                                      # If left is not None (prioritize left path)
        return goLeft                                               # Return the value and the path
    else:                                                           # Else, return right
        return goRight                                              #
                                                                    #
def deepPath(node, path, targetDepth):                              # Supportive function
    if not node:                                                    # If there is no node
        return None                                                 # Return None
    layer = path.count('.') + 1                                     # The layer is 1 more than the number of dots
    if layer == targetDepth:                                        # If this is the targeted node
        return (node.value, path)                                   # Return the value and the path to here
    else:                                                           # Otherwise
        goLeft = deepPath(node.left, path + '.left', targetDepth)   # Check left and right
        goRight = deepPath(node.right, path + '.right', targetDepth)# Add new direction to the path
    if goLeft:                                                      # Similarly, prioritize the left side
        return goLeft                                               # if possible
    else:                                                           #
        return goRight                                              #
                                                                    #
def depth(node):                                                    # Supportive function
    if not node:                                                    # If there is no node here
        return 0                                                    # Return 0
    goLeft = depth(node.left) + 1                                   # Otherwise go left and right
    goRight = depth(node.right) + 1                                 # Depth is 1 step further than current level
    return max(goLeft, goRight)                                     # Return the deeper side


# In[4]:


print('Given the tree below')
print('     a\n    / \\\n   a   a\n  /   / \\\n a   a   a\n    /   / \\\n   a   a   a\n      /\n     b')


# In[5]:


a, b = deepestNode(node_a)
print('The deepest node is "{}", the path is "{}" and it is at level {}'.format(a, b, b.count('.') + 1))


# In[6]:


print('Given the tree below')
print('     a\n    / \\\n   b   c\n  /\n d')


# In[7]:


a, b = deepestNode(node_b)
print('The deepest node is "{}", the path is "{}" and it is at level {}'.format(a, b, b.count('.') + 1))

