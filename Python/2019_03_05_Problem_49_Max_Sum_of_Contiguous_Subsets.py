#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 5th
# 
# Problem: Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# 
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# 
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
# 
# Do this in O(N) time.

# In[37]:


def max_sum_contiguous(lst, sum_ = None):                          #
    local_max = []                                                 # Keep a local max, for each subset
    global_max = [0]                                               # And a global max for every subsets
    for e in lst:                                                  # For each element
        local_max = [[e] ,local_max + [e]][sum(local_max) + e > e] # Choose if adding it to the previous
                                                                   # or start a new chain is bigger
        global_max = [local_max, global_max][sum(global_max) > sum(local_max)] # Update global max
    return sum(global_max) if sum_ == True else global_max         #


# In[13]:


l1 = [34, -50, 42, 14, -5, 86]
l2 = [-5, -1, -8, -9]
l3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# In[39]:


print('Given the 3 sets {}, {} and {}'.format(l1, l2, l3))
print('The maximum contiguous subsets are {}, {} and {}'.format(max_sum_contiguous(l1),
                                                               max_sum_contiguous(l2),
                                                               max_sum_contiguous(l3)))
print('The sum values are {}, {} and {}'.format(max_sum_contiguous(l1, sum_ = True),
                                               max_sum_contiguous(l2, sum_ = True),
                                               max_sum_contiguous(l3, sum_ = True)))

