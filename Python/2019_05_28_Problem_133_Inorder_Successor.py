#!/usr/bin/env python
# coding: utf-8
"""2019 May 28th - Daily_Coding_Problem #133."""
# <markdown>
# ## 2019 May 28th - Daily_Coding_Problem #133
#
# Problem: Given a node in a binary search tree,
# return the next bigger element, also known as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
# `  10
#   /  \
#  5    30
#      /  \
#    22    35
#
# You can assume each node has a parent pointer.


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

    def inorderList(self):
        """Return an ordered list of nodes."""
        if not self:
            return None
        listNodes = [self]
        if self.left:
            listNodes = self.left.inorderList() + listNodes
        if self.right:
            listNodes = listNodes + self.right.inorderList()
        return listNodes


def inorderSuccessor(node):
    """Return the next bigger element."""
    root = node
    while root.parent:
        root = root.parent
    listNodes = root.inorderList()
    for i in range(len(listNodes)):
        if listNodes[i] == node:
            if i+1 == len(listNodes):
                return None
            return listNodes[i+1]


# %%
left = Node(5)
right = Node(30, Node(22), Node(35))
binarySearchTree = Node(10, left, right)
# %%
inorderSuccessor(left).value
