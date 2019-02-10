#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 10th
# 
# Problem: Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
# 
# The list is very long, so making more than one pass is prohibitively expensive.
# 
# Do this in constant space and in one pass.

# In[96]:


def remove_kth_last(lst, k):
    for i, e in enumerate(reversed(lst)):
        # Counting backward start from 1 not 0
        if i == k:
            rm = lst.pop(e)
    return rm, lst


# In[97]:


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
k = 4
print('Given the examplt list: {}'.format(l))
rm, l = remove_kth_last(l, k)
print('Remove the {}th last number, which is {}, returned: {}'.format(k, rm, l))

