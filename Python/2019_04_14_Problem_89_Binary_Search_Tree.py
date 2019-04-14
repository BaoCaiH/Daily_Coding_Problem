#!/usr/bin/env python
# coding: utf-8

# ### 2019 April 14th
# 
# Problem: Determine whether a tree is a valid binary search tree.
# 
# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

# In[111]:


class Node:                                                 #
    def __init__(self, value, left = None, right = None):   #
        self.value = value                                  #
        self.left = left                                    #
        self.right = right                                  #
                                                            #
def isBinarySearchTree(root):                               #
                                                            #
    def isBinarySearchTreeHelper(node):                     # This will return the value of the node if it is
        if not node:                                        # a binary search tree
            return None                                     # If there is no node, return nothing
        value = node.value                                  # Store the value
        if node.left and node.right:                        # If both children are available
            left = isBinarySearchTreeHelper(node.left)      # Run the function on the left node
            right = isBinarySearchTreeHelper(node.right)    # Run the function on the right node
            if left is not None and right is not None:      # If both children are valid
                if left < value and right > value:          # Check the rule on the values
                    return value                            # If true, then return the node value
                else:                                       # Otherwise
                    return None                             # Return nothing
            else:                                           # If either or both children are not valid
                return None                                 # Return nothing
        elif not node.left and not node.right:              # If there is no children
            return value                                    # Return the value
        else:                                               # If there is one child on either side
            return None                                     # Return nothing
                                                            #
    return ['invalid', 'valid'][bool(isBinarySearchTreeHelper(root))]# Run the helper and return validity


# In[112]:


nodeA = Node(10, Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8))),
             Node(15, Node(13, Node(12), Node(14)), Node(17, Node(16), Node(18))))


# In[113]:


nodeB = Node(10, Node(5, Node(3, Node(4), Node(4)), Node(7, Node(8), Node(8))),
             Node(15, Node(13, Node(12), Node(14)), Node(17, Node(16), Node(18))))


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




