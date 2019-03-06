#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 6th
# 
# Problem: Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
# 
# Given the root to such a tree, write a function to evaluate it.
# 
# For example, given the following tree:
# 
# `\  *
#    / \
# \ +   +
#  /\   /\
# 3  2 4  5`
# 
# You should return 45, as it is (3 + 2) * (4 + 5).

# In[1]:


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# In[26]:


a = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
b = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4)))
c = Node('/', Node('+', Node(4), Node(5)), Node('-', Node('*', Node(8), Node(2))))


# In[24]:


def arithmetic(tree):                          #
    if not tree:                               # If the node is not available
        return None                            # Return None
    left = arithmetic(tree.left)               # Calculate the left side of the node
    right = arithmetic(tree.right)             # And the right side
    if tree.val == '+':                        # If the node is a addition function
        if left is None or right is None:      # but if either of them is None, return the other
            return [left, right][left is None] # (if both are None, it does not matter which one we return)
        return left + right                    # If both are not None, perform addition
    if tree.val == '-':                        # If subtraction
        if left is None or right is None:      #
            return [left, right][left is None] #
        return left - right                    # Perform subtraction, left to right
    if tree.val == '*':                        # If multiplication
        if left is None or right is None:      #
            return [left, right][left is None] #
        return left * right                    # Perform multiplication
    if tree.val == '/':                        # If division
        if left is None or right is None:      #
            return [left, right][left is None] #
        return left / right                    # Perform division
    return tree.val                            # If neither, means it's a number, return the number
        


# In[58]:


print('Given the tree below:')
print('    *\n   / \\\n  +   +\n /\\   /\\\n3  2 4  5')
print('That is (3 + 2) * (4 + 5) = 5*9')
print('The evaluation returned {}'.format(arithmetic(a)))


# In[59]:


print('Given the tree below:')
print('    *\n   / \\\n  +   +\n /\\   /\n3  2 4')
print('That is (3 + 2) * 4 = 5*4')
print('The evaluation returned {}'.format(arithmetic(b)))


# In[57]:


print('Given the tree below:')
print('    /\n   / \\\n  +   -\n /\\   /\n4  5 *\n     /\\\n    2  8')
print('That is (4 + 5) / (2 * 8) = 9/16')
print('The evaluation returned {}'.format(arithmetic(c)))

