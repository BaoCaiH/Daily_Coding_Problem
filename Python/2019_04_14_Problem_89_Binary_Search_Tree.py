#!/usr/bin/env python
# coding: utf-8
"""2019 April 14th - Daily_Coding_Problem #189."""
# ### 2019 April 14th
# %% markdown
# Problem: Determine whether a tree is a valid binary search tree.
#
# A binary search tree is a tree with two children, left and right,
# and satisfies the constraint that the key in the left child must be
# less than or equal to the root and the key in the right child must be
# greater than or equal to the root.

# In[111]:


class Node:
    """A node class for the binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize a node for a binary tree."""
        self.value = value
        self.left = left
        self.right = right


def isBinarySearchTree(root):
    """Check if the binray tree is a binary search tree."""
    def isBinarySearchTreeHelper(node):
        if not node:
            return None
        listNodes = [node]
        if node.left:
            listNodes = isBinarySearchTreeHelper(node.left) + listNodes
        if node.right:
            listNodes = listNodes + isBinarySearchTreeHelper(node.right)
        return listNodes

    listNodes = isBinarySearchTreeHelper(root)
    curr = listNodes[0]
    for i in range(1, len(listNodes)):
        if curr.value > listNodes[i].value:
            return False
        curr = listNodes[i]
    return True


# In[112]:


nodeA = Node(10, Node(5, Node(3, Node(2), Node(4)),
             Node(7, Node(6), Node(8))),
             Node(15, Node(13, Node(12), Node(14)),
             Node(17, Node(16), Node(18))))


# In[113]:


nodeB = Node(10, Node(5, Node(3, Node(4), Node(4)),
             Node(7, Node(8), Node(8))),
             Node(15, Node(13, Node(12), Node(14)),
             Node(17, Node(16), Node(18))))


# In[114]:


isBinarySearchTree(nodeA)


# In[104]:


print('Given the following trees:')
print('Tree A:')
print('          10\n        /   \\\n       /     \\\n      /       \\\n     5         15\n   /  \\      /    \\\n  3    7    13     17\n /\\   /\\    /\\     /\\\n2  4 6  8 12  14 16  18')


# In[105]:


print('And Tree B:')
print('          10\n        /   \\\n       /     \\\n      /       \\\n     5         15\n   /  \\      /    \\\n  3    7    13     17\n /\\   /\\    /\\     /\\\n4  4 8  8 12  14 16  18')


# In[115]:


print('Tree A is a {} binary search tree'.format(isBinarySearchTree(nodeA)))
print('Tree B is an {} binary search tree'.format(isBinarySearchTree(nodeB)))
print('Because although the upper level of the tree is valid, the lower level caused the whole left branch invalid')


# In[ ]:
