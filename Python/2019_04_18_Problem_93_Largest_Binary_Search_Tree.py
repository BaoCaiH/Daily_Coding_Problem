#!/usr/bin/env python
# coding: utf-8
"""2019 April 18th - Daily_Coding_Problem #93."""
# <markdown>
# ## 2019 April 18th - Daily_Coding_Problem #93

# Problem: Given a tree, find the largest tree/subtree that is a BST.

# Given a tree, return the size of the largest tree/subtree that is a BST.

# <codecell>
print('Testing Python on Atom')

# <codecell>


class Node:
    """
    This is the class for storing the binary tree.

    Each value is stored as a node with value, and left and right nodes.
    """

    def __init__(self, value, left=None, right=None):
        """Initialize the node."""
        self.value = value
        self.left = left
        self.right = right


def isBinarySearchTree(node):
    """Return the validity of a binary tree."""
    if not node:
        return None
    value = node.value
    if node.left and node.right:
        left = isBinarySearchTree(node.left)
        right = isBinarySearchTree(node.right)
        if left is not None and right is not None:
            if left < value and right > value:
                return value
            else:
                return None
        else:
            return None
    elif not node.left and not node.right:
        return value
    else:
        return None


def binarySearchTreeSize(node):
    """Return the size of a binary search tree."""
    if not node:
        return 0
    if not node.left and not node.right:
        return 0
    return 1 + binarySearchTreeSize(node.left) +\
        binarySearchTreeSize(node.right)


def largestBinarySearchTree(root, maxSize=0):
    """Return the largest possible binary tree size."""
    if not root:
        return 0
    if isBinarySearchTree(root):
        nodeSize = binarySearchTreeSize(root)
    else:
        nodeSize = 0
    maxLeft = largestBinarySearchTree(root.left)
    maxRight = largestBinarySearchTree(root.right)

    return max([maxSize, nodeSize, maxLeft, maxRight])

# <codecell>


nodeB = Node(10, Node(5, Node(3, Node(4), Node(4)),
             Node(7, Node(8), Node(8))),
             Node(15, Node(13, Node(12), Node(14)),
             Node(17, Node(16), Node(18))))

# <codecell>
print('Given the binary tree:')
print('          10')
print('        /   \\\n       /     \\\n      /       \\')
print('     5         15\n   /  \\      /    \\')
print('  3    7    13     17')
print(' /\\   /\\    /\\     /\\\n4  4 8  8 12  14 16  18')

# <codecell>
print('Largest binary search tree size is {}'.
      format(largestBinarySearchTree(nodeB)))
