#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 2nd
# 
# Problem: Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
# 
# The input list is not necessarily ordered in any way.
# 
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

# In[12]:


def overlapping_intervals(lst):             #
    lst.sort()                              # Sort the intervals first
    non_overlapping = []                    # Empty list
    for i, e in enumerate(lst):             # For each interval
        if not non_overlapping:             # If it's the first interval
            non_overlapping.append(e)       # Add it in
        else:                               # Otherwise
            if e[0] >= lst[i-1][1]:         # Only add the interval if the current start is more than previous end
                non_overlapping.append(e)   #
    return non_overlapping                  #


# In[10]:


a = [(1, 3), (5, 8), (4, 10), (20, 25)]


# In[11]:


overlapping_intervals(a)

