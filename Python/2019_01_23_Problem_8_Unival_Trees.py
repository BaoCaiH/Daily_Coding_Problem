#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 23rd
# 
# Problem: A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees (at all the 1 and the 0):
# 
# `> 0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1`

# In[49]:


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# In[134]:


tree_1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
tree_2 = Node('a', Node('c'), Node('b', Node('b'), Node('b', right = Node('b'))))
tree_3 = Node('a', Node('a'), Node('a', Node('a'), Node('a', right = Node('A'))))


# In[198]:


def unival_counter(tree):
    # First turn each node in the tree into indicators, whether it is a root of a unival tree or not
    def is_unival_node(node):
        # Only when the node exist
        if node is not None:
            # If the node does not have any leaf, it is unival
            if node.left == None and node.right == None:
                return Node(1)
            # If it has both leaves
            elif node.left is not None and node.right is not None:
                # If they are equal to each other
                if node.left.val == node.right.val == node.val:
                    # Hold it, we still need to check its leaves
                    # If the leaves are also unival 1 * 1 = 1 then it is unival
                    # If either leaves are not, then 0 * anything = 0, not unival
                    return Node(compare_value(node.left).val * compare_value(node.right).val, compare_value(node.left), compare_value(node.right))
                
                # Not equal? Nothing else to say, just 0
                else:
                    return Node(0, compare_value(node.left), compare_value(node.right))
            # Similar to the both leaves case, but now one does not exist
            # So the value of the node is either 0 or equal to the value of the existing leaf
            elif node.left is None and node.right is not None:
                if node.val != node.right.val:
                    return Node(0, right =  compare_value(node.right))
                else:
                    return Node(compare_value(node.right).val, right =  compare_value(node.right))
            # Same as above
            elif node.right is None and node.left is not None:
                if node.val != node.left.val:
                    return Node(0, left = compare_value(node.left))
                else:
                    return Node(compare_value(node.left).val, left = compare_value(node.left))

    def counter(node):
        # This is the simple step
        # Just sum up everything
        count = 0
        if node is not None:
            count += node.val + counter(node.left) + counter(node.right)
        return count
    
    return counter(is_unival_node(tree))


# In[197]:


print('Given the first tree below:')
print('>  0\n  / \\\n 1   0\n    / \\\n   1   0\n  / \\\n 1   1')
print('There are {} unival tree in here'.format(unival_counter(tree_1)))


# In[195]:


print('Given another tree below:')
print('>  a\n  / \\\n c   b\n    / \\\n   b   b\n        \\\n         b')
print('There are {} unival trees in here'.format(unival_counter(tree_2)))


# In[196]:


print('Given yet another tree below:')
print('>  a\n  / \\\n a   a\n    / \\\n   a   a\n        \\\n         A')
print('There are {} unival trees in here'.format(unival_counter(tree_3)))

