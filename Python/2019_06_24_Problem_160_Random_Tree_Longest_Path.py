#!/usr/bin/env python
# coding: utf-8
"""2019 June 24th - Daily_Coding_Problem #160."""
# <markdown>
# ## 2019 June 24th - Daily_Coding_Problem #160
#
# This problem was asked by Uber.
#
# Given a tree where each edge has a weight,
# compute the length of the longest path in the tree.
#
# For example, given the following tree:
#
# `   a
#   /|\
#  b c d
#     / \
#    e   f
#   / \
#  g   h`
#
# and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1,
# the longest path would be c -> a -> d -> f, with a length of 17.
#
# The path does not have to pass through the root,
# and each node can have any amount of children.


# %%
class Node:
    """Node class with distance to children."""

    def __init__(self, name):
        """Initialize the Node."""
        self.name = name
        self.longest = None
        self.branches = []


def longestStraightPath(root):
    """Record the longest straight path from each node to the tree end."""
    if not root.branches:
        root.longest = 0
        return root.longest
    distLst = []
    for distance, branch in root.branches:
        distLst.append(distance + longestStraightPath(branch))
    root.longest = max(distLst)
    return root.longest


# %%
def longestPath(root):
    """Get the longest path through a random tree."""
    if root.longest is None:
        longestStraightPath(root)
    if not root.branches:
        return root.longest
    branchDistLst = []
    straightDistLst = []
    for distance, branch in root.branches:
        straightDistLst.append(distance + branch.longest)
        branchDistLst.append(longestPath(branch))
    longestBranch = max(branchDistLst)
    return max(sum(sorted(straightDistLst)[-2:]), longestBranch)


# %%
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
a.branches.append((3, b))
a.branches.append((5, c))
a.branches.append((8, d))
d.branches.append((2, e))
d.branches.append((4, f))
e.branches.append((1, g))
e.branches.append((1, h))
# %%
longestPath(a)
