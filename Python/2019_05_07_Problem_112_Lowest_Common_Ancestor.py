#!/usr/bin/env python
# coding: utf-8
"""2019 May 7th - Daily_Coding_Problem #112."""
# <markdown>
# ## 2019 May 7th - Daily_Coding_Problem #112
#
# Problem: Given a binary tree, find the lowest common ancestor (LCA) of
# two given nodes in the tree.
# Assume that each node in the tree also has a pointer to its parent.


# %%
class Node:
    """The binary tree node object."""

    def __init__(self, value, left=None, right=None):
        """Initialize the tree node."""
        self.parent = None
        self.value = value
        self.left = left
        self.right = right
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self


# %%
def LCA(nodeA, nodeB):
    """Find the lowest common ancestor of 2 nodes."""
    def findAllAncestors(node):
        ancestors = []
        while node:
            ancestors.append(node.value)
            node = node.parent
        return ancestors
    ancestorsA = findAllAncestors(nodeA)
    ancestorsB = findAllAncestors(nodeB)
    if len(ancestorsA) >= len(ancestorsB):
        for v in ancestorsA:
            if v in ancestorsB:
                break
        steps = ancestorsB.index(v)
        i = 0
        while i < steps:
            nodeB = nodeB.parent
            i += 1
        return nodeB
    else:
        for v in ancestorsB:
            if v in ancestorsA:
                break
        steps = ancestorsA.index(v)
        i = 0
        while i < steps:
            nodeA = nodeA.parent
            i += 1
        return nodeA


# %%
node2 = Node('2')
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1 = Node(1, node2, node3)
node3.left = node4
node3.right = node5
node4.parent = node3
node5.parent = node3


# %%
LCA(node2, node4).value
