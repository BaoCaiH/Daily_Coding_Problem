#!/usr/bin/env python
# coding: utf-8
"""2019 July 13th - Daily_Coding_Problem #179."""
# <markdown>
# ## 2019 July 13th - Daily_Coding_Problem #179
#
# This problem was asked by Google.
#
# Given the sequence of keys visited by a postorder traversal of
# a binary search tree, reconstruct the tree.
#
# For example, given the sequence `2, 4, 3, 8, 7, 5`,
# you should construct the following tree:
#
# `    5
#    / \
#   3   7
#  / \   \
# 2   4   8`


# %%
class Node:
    """Create a node class."""

    def __init__(self, value, left=None, right=None):
        """Initialize a new node."""
        self.value = value
        self.left = left
        self.right = right


def addNode(head, value):
    """Add a new node to the appropiate place in the binary search tree."""
    while head:
        if value >= head.value:
            if not head.right:
                head.right = Node(value)
                print('Added {} to the right of {}'.format(value, head.value))
                break
            else:
                head = head.right
        else:
            if not head.left:
                head.left = Node(value)
                print('Added {} to the left of {}'.format(value, head.value))
                break
            else:
                head = head.left


def reconstruct(sequence):
    """Reconstruct the binary search tree from the given sequence."""
    nNode = len(sequence)
    head = Node(sequence[-1])
    print('The head node is {}'.format(head.value))
    for i in range(nNode-2, -1, -1):
        addNode(head, sequence[i])
    return head


# %%
sequence = [2, 4, 3, 8, 7, 5]
n = reconstruct(sequence)
