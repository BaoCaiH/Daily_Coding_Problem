#!/usr/bin/env python
# coding: utf-8
"""2019 May 11th - Daily_Coding_Problem #116."""
# <markdown>
# ## 2019 May 11th - Daily_Coding_Problem #116
#
# Problem: Generate a finite,
# but an arbitrarily large binary tree quickly in O(1).
#
# That is, generate() should return a tree whose size is unbounded but finite.


# %%
# %%
class Node:
    """Node class for a binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize the node."""
        self.parent = None
        self.value = value
        self._left = left
        self._right = right
        self.isLeftEvaluate = False
        self.isRightEvaluate = False
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    @property
    def left(self, value=None):
        """Return the left node, create if empty."""
        import random
        if not self.isLeftEvaluate:
            if random.random() < 0.5:
                value = random.randint(0, 100)
                self._left = Node(value)
            self.isLeftEvaluate = True
        return self._left

    @property
    def right(self, value=None):
        """Return the right node, create if empty."""
        import random
        if not self.isRightEvaluate:
            if random.random() < 0.5:
                value = random.randint(0, 100)
                self._right = Node(value)
            self.isRightEvaluate = True
        return self._right

    def deconstruct(self, level='@'):
        """Deconstruct the binary tree into a string."""
        sub = []
        if self.left:
            sub = sub + self.left.deconstruct(level + '@')
        if self.right:
            sub = sub + self.right.deconstruct(level + '@')
        return [level] + [self.value] + sub
    #
    # def printLevelWise(self):
    #     """Print the binary tree level-wise."""
    #     treeInString = self.deconstruct()
    #     layers = {}
    #     for e in treeInString:
    #         try:
    #             if '@' in e:
    #                 count = e.count('@')
    #             else:
    #                 if count not in layers:
    #                     layers[count] = []
    #                 layers[count].append(e)
    #         except TypeError:
    #             if count not in layers:
    #                 layers[count] = []
    #             layers[count].append(e)
    #     printing = []
    #     for value in layers.values():
    #         printing = printing + value
    #     return printing
    #
    # def rootToLeaves(self, path=[]):
    #     """Print every paths from root to leaves."""
    #     if not self:
    #         return path
    #     paths = []
    #     if not self.left and not self.right:
    #         return [path + [self.value]]
    #     if self.left:
    #         paths = paths + self.left.rootToLeaves(path + [self.value])
    #     if self.right:
    #         paths = paths + self.right.rootToLeaves(path + [self.value])
    #     return paths


def generate():
    """Return a finite but arbitrary large binary tree."""
    return Node(0)


# %%
node = generate()
node.deconstruct()
