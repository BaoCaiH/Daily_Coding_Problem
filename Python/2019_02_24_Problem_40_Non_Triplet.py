#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 24th
# 
# Problem: This problem was asked by Google.
# 
# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
# 
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
# 
# Do this in O(N) time and O(1) space.

# In[112]:


def non_triplet(lst):
    return int(((sum(set(lst))) * 3 - sum(lst)) / 2)


# In[110]:


l1 = [6, 1, 3, 3, 3, 6, 6]
l2 = [13, 19, 13, 13]


# In[117]:


print('This solution is solve by mathematics and it is not space efficient, only time efficient')
print('The set of number will include a subset of triplets and a single number')
print('Meaning: sum_of_the_set = 3 * (distinct_numbers_from_the_triplets) + the_single_number')
print('the_single_number = (3 * all_distinct_numbers - sum_of_the_set) / 2')
print('')
print('Given the two sets {} and {}'.format(l1, l2))
print('The single numbers are {} and {}'.format(non_triplet(l1), non_triplet(l2)))

