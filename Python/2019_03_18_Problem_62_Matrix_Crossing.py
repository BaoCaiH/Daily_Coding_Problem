#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 18th
# 
# Problem: There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.
# 
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
# 
# Right, then down<br>
# Down, then right
# 
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

# In[31]:


def cross_matrix(n, m, x = 0, y = 0):                   #
    if x == n - 1 or y == m - 1:                        # If the position is either at right side wall or bottom
        return 1                                        # There is only 1 option is to head straight to the goal
    else:                                               # Otherwise
        return cross_matrix(n, m, x = x + 1, y = y) +                cross_matrix(n, m, x = x, y = y + 1)    # Recurse on both direction


# In[32]:


n = int(input('Give an "N" dimension for the matrix: '))
m = int(input('Give an "M" dimension for the matrix: '))
print('There are {} ways to get to the bottom-right of a {} by {} matrix'.format(cross_matrix(n, m), n, m))

