#!/usr/bin/env python
# coding: utf-8
"""2019 June 10th - Daily_Coding_Problem #146."""
# <markdown>
# ## 2019 June 10th - Daily_Coding_Problem #146
#
# This question was asked by BufferBox.

# Given a binary tree where all nodes are either 0 or 1,
# prune the tree so that subtrees containing all 0s are removed.
#
# For example, given the following tree:
#
# `   0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0`
#
# should be pruned to:
#
# `   0
#   / \
#  1   0
#     /
#    1`
#
# We do not remove the tree at the root or its left child
# because it still has a 1 as a descendant.


# %%
class Node:
    """Node class for a binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize the node."""
        self.parent = None
        self.value = value
        self.left = left
        self.right = right
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def branchTotal(self):
        """Sum all the value in a branch."""
        total = self.value
        if self.left:
            total = total + self.left.branchTotal()
        if self.right:
            total = total + self.right.branchTotal()
        return total

    def pruneBranch(self):
        """Prune all branches which have 0 sum."""
        if not self:
            return None
        if self.branchTotal() == 0:
            return None
        if self.left:
            self.left = self.left.pruneBranch()
        if self.right:
            self.right = self.right.pruneBranch()
        return self

    def deconstruct(self, level='@'):
        """Deconstruct the binary tree into a string."""
        sub = []
        if self.left:
            sub = sub + self.left.deconstruct(level + '@')
        if self.right:
            sub = sub + self.right.deconstruct(level + '@')
        return [level] + [self.value] + sub

    def printLevelWise(self):
        """Print the binary tree level-wise."""
        treeInString = self.deconstruct()
        layers = {}
        for e in treeInString:
            try:
                if '@' in e:
                    count = e.count('@')
                else:
                    if count not in layers:
                        layers[count] = []
                    layers[count].append(e)
            except TypeError:
                if count not in layers:
                    layers[count] = []
                layers[count].append(e)
        printing = []
        for value in layers.values():
            printing = printing + value
        return printing


# %%
biTree = Node(0, Node(1), Node(0,
              Node(1, Node(0), Node(0)), Node(0)))
# %%
biTree.deconstruct()
# %%
biTree.pruneBranch()
# %%
biTree.right.left.value
# %%
biTree.deconstruct()
