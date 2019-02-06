#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 28th - bonus
# 
# Problem: Given the root to a binary tree, return the deepest node.

# In[1]:


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


# In[118]:


node_a = Node('a', Node('a', Node('a', Node('a'))), Node('a', Node('a'), Node('a', Node('a', Node('b')), Node('a'))))


# In[114]:


def deepest_node(root):
    def node_max(node, layer = None):
        if layer is None:
            layer = 1
        if node is not None:
            return max(layer,                                   # Compare all the layers to find the max layer
                       node_max(node.left, layer + 1),
                       node_max(node.right, layer + 1))
        else:
            return 0
    max_node = node_max(root)
    print(max_node)
    def call_deepest(node, side = '', layer = None):
        if layer is None:
            layer = 1
        if node is not None:
            deep.append((str(node.value), side, layer))         # Write all the value, position and layer into a list of tuples
            call_deepest(node.left, side + '.left', layer + 1)  # and repeat until finish
            call_deepest(node.right, side + '.right', layer + 1)
    deep = []
    call_deepest(root)
    for tup in deep:
        if tup[2] == max_node:                                  # Take out the max one
            return tup


# In[119]:


a, b, c = deepest_node(node_a)


# In[123]:


print('Given the tree below')
print('     a\n    / \\\n   a   a\n  /   / \\\n a   a   a\n    /   / \\\n   a   a   a\n      /\n     b')
print('The deepest node has the value \'{}\' at layer number {} at the position {}'.format(a, b, c))

