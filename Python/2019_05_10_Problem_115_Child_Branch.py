#!/usr/bin/env python
# coding: utf-8
"""2019 May 10th - Daily_Coding_Problem #115."""
# <markdown>
# ## 2019 May 10th - Daily_Coding_Problem #115
#
# Problem: Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and
# node values with a subtree of s. A subtree of s is a tree consists of
# a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


# %%
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


def isChildBranch(parent, maybeChild):
    """Check if the second tree is a branch of the first."""
    if not parent or not maybeChild:
        return False
    if parent.deconstruct() == maybeChild.deconstruct():
        return True
    else:
        if any([isChildBranch(parent.left, maybeChild),
                isChildBranch(parent.right, maybeChild)]):
            return True
        return False


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
node6 = Node('giberish')

# %%
isChildBranch(node1, node6)
