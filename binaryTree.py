#!/usr/bin/env python
# coding: utf-8
"""A binary tree with collective methods."""
# <markdown>
# For future use of course


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

    # These too
    # @property
    # def left(self, value=None):
    #     """Return the left node, create if empty."""
    #     import random
    #     if not self.isLeftEvaluate:
    #         if random.random() < 0.5:
    #             value = random.randint(0, 100)
    #             self._left = Node(value)
    #         self.isLeftEvaluate = True
    #     return self._left
    #
    # @property
    # def right(self, value=None):
    #     """Return the right node, create if empty."""
    #     import random
    #     if not self.isRightEvaluate:
    #         if random.random() < 0.5:
    #             value = random.randint(0, 100)
    #             self._right = Node(value)
    #         self.isRightEvaluate = True
    #     return self._right

    def deconstruct(self, level='@'):
        """Deconstruct the binary tree into a string."""
        sub = []
        if self.left:
            sub = sub + self.left.deconstruct(level + '@')
        if self.right:
            sub = sub + self.right.deconstruct(level + '@')
        return [level] + [self.value] + sub

    def nodeValues(self):
        """Get all the values in the tree."""
        vals = [self.value]
        if self.left:
            vals = vals + self.left.nodeValues()
        if self.right:
            vals = vals + self.right.nodeValues()
        return vals

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
