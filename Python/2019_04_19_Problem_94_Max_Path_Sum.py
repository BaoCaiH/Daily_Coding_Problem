#!/usr/bin/env python
# coding: utf-8
"""2019 April 19th - Daily_Coding_Problem #94."""
# <markdown>
# ## 2019 April 19th - Daily_Coding_Problem #94

# Problem: Given a binary tree of integers, find the maximum path sum
# between two nodes. The path must go through at least one node,
# and does not need to go through the root.


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


def maxPathSum(node, currentSum=0, maxSum=0):
    """Return the maximum path sum."""
    if not node:
        return currentSum
    # Continue path or start a new
    currentSum = max(currentSum + node.value,
                     node.value)
    # Update max
    maxSum = max(currentSum, maxSum)
    # Return the max between current max, left and right paths
    leftSum = maxPathSum(node.left, currentSum, maxSum)
    rightSum = maxPathSum(node.right, currentSum, maxSum)
    return max(maxSum, leftSum, rightSum)


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
print('The max path sum is {}'.format(maxPathSum(nodeB)))

# <codecell>
nodeA = Node(5, Node(5, Node(0, Node(-8), Node(0)),
             Node(-2, Node(-6), Node(-1))),
             Node(-3, Node(6, Node(-2), Node(0)),
             Node(3, Node(-9), Node(7))))

# <codecell>
print('Given the binary tree:')
print('            5')
print('          /   \\')
print('         /     \\')
print('        /       \\')
print('       /         \\')
print('      5          -3')
print('     / \\          /\\')
print('    /   \\        /  \\')
print('   0    -2      6    3')
print('  /\\    / \\    /\\    /\\')
print('-8  0 -6  -1 -2  0 -9  7')

# <codecell>
print('The max path sum is {}'.format(maxPathSum(nodeA)))
