#!/usr/bin/env python
# coding: utf-8
"""2019 May 12th - Daily_Coding_Problem #117."""
# <markdown>
# ## 2019 May 12th - Daily_Coding_Problem #117
#
# Problem: Given a binary tree, return the level of the tree with minimum sum.


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

    def deconstruct(self, level='@'):
        """Deconstruct the binary tree into a string."""
        sub = []
        if self.left:
            sub = sub + self.left.deconstruct(level + '@')
        if self.right:
            sub = sub + self.right.deconstruct(level + '@')
        return [level] + [self.value] + sub

    def minimumLevel(self):
        """Print the level with minimum sum."""
        treeInString = self.deconstruct()
        layers = {}
        for e in treeInString:
            try:
                if '@' in e:
                    count = e.count('@')
                else:
                    if count not in layers:
                        layers[count] = 0
                    layers[count] += e
            except TypeError:
                if count not in layers:
                    layers[count] = 0
                layers[count] += e
        minSum = min(layers.values())
        return list(layers.values()).index(minSum)


# %%
nodeB = Node(100, Node(5, Node(3, Node(4), Node(4)),
             Node(7, Node(8), Node(8))),
             Node(15, Node(13, Node(12), Node(14)),
             Node(17, Node(16), Node(18))))

print('Given the binary tree:')
print('          100')
print('        /   \\\n       /     \\\n      /       \\')
print('     5         15\n   /  \\      /    \\')
print('  3    7    13     17')
print(' /\\   /\\    /\\     /\\\n4  4 8  8 12  14 16  18')
# %%
nodeB.minimumLevel()
