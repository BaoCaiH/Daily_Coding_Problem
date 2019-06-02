#!/usr/bin/env python
# coding: utf-8
"""2019 May 30th - Daily_Coding_Problem #135."""
# <markdown>
# ## 2019 May 30th - Daily_Coding_Problem #135
#
# Problem: Given a binary tree, find a minimum path sum from root to a leaf.
#
# For example, the minimum path in this tree is [10, 5, 1, -1],
# which has sum 15.
#
# `  10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1`


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

    def minimumPath(self):
        """Find the minimmum path from root to leaves."""
        paths = self.rootToLeaves()
        minPath = None
        minDistance = None
        for path in paths:
            if not minPath:
                minPath = path
                minDistance = sum(minPath)
            else:
                if sum(path) < minDistance:
                    minPath = path
                    minDistance = sum(minPath)
        return minPath


# %%
tree = Node(10, Node(5, right=Node(2)),
            Node(5, right=Node(1, Node(-1))))
tree.minimumPath()
