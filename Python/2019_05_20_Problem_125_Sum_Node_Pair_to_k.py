#!/usr/bin/env python
# coding: utf-8
"""2019 May 20th - Daily_Coding_Problem #125."""
# <markdown>
# ## 2019 May 20th - Daily_Coding_Problem #125
#
# Problem: Given the root of a binary search tree, and a target K,
# return two nodes in the tree whose sum equals K.
#
# For example, given the following tree and K of 20
#
# `    10
#    /   \
#  5      15
#        /  \
#      11    15`
#
# Return the nodes 5 and 15.


# %%
class Node:
    """Node class for a binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize the node."""
        self.parent = None
        self.value = value
        self.left = left
        self.right = right
        # Uncomment these lines for auto-generation of tree
        # self._left = left
        # self._right = right
        # self.isLeftEvaluate = False
        # self.isRightEvaluate = False
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def nodeValues(self):
        """Get all the values in the tree."""
        vals = [self.value]
        if self.left:
            vals = vals + self.left.nodeValues()
        if self.right:
            vals = vals + self.right.nodeValues()
        return vals


def nodePair(tree, k):
    """Return the 2 node values add up to k."""
    vals = tree.nodeValues()
    for i, v in enumerate(vals):
        if v <= k and k-v in vals[:i] + vals[i+1:]:
            return (v, k-v)


# %%
node = Node(10, Node(5), Node(15, Node(11), Node(15)))
# %%
nodePair(node, 21)
