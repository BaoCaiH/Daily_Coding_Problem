#!/usr/bin/env python
# coding: utf-8
"""2019 May 5th - Daily_Coding_Problem #110."""
# <markdown>
# ## 2019 May 5th - Daily_Coding_Problem #110
#
# Problem: Given a binary tree, return all paths from the root to leaves.
#
# For example, given the tree:
#
# ` 1
#  / \
# 2   3
#    / \
#   4   5`
#
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].


# %%
# %%
class Node:
    """Node class for a binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize the node."""
        self.value = value
        self.left = left
        self.right = right

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

    def rootToLeaves(self, path=[]):
        """Print every paths from root to leaves."""
        if not self:
            return path
        paths = []
        if not self.left and not self.right:
            return [path + [self.value]]
        if self.left:
            paths = paths + self.left.rootToLeaves(path + [self.value])
        if self.right:
            paths = paths + self.right.rootToLeaves(path + [self.value])
        return paths


# %%
node1 = Node(1, Node('2'), Node(3, Node(4), Node(5)))

# %%
node1.rootToLeaves()
