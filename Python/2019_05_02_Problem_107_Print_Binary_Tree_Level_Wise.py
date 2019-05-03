#!/usr/bin/env python
# coding: utf-8
"""2019 May 2nd - Daily_Coding_Problem #107."""
# <markdown>
# ## 2019 May 2nd - Daily_Coding_Problem #107
#
# Problem: Print the nodes in a binary tree level-wise.
# For example, the following should print 1, 2, 3, 4, 5.
#
# ` 1
#  / \
# 2   3
#    / \
#   4   5`


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


# %%
node1 = Node(1, Node('2'), Node(3, Node(4), Node(5)))

# %%
node1.printLevelWise()
