#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 26th
# 
# Problem: Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
# 
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
# 
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

# In[90]:


def reach_target(s, k):
    if len(s) == 1:                                        # If the set is only 1 element long
        if s[0] == k:                                      # If that element is the target number
            return [k]                                     # Good
        else:                                              # If not
            return None                                    # Bad
                                                           # Otherwise, real work here
    for i, num in enumerate(s):                            # For each number
        if num == k:                                       # If it's magically equal to the target
            return [num]                                   # Great
        elif num < k:                                      # Otherwise it should less than the target
            subs = reach_target(s[:i] + s[i+1:], k - num)  # Recurse the function with a subset
                                                           # without the number, and a smaller target
            if subs:                                       # If it returns anything at all
                                                           # (otherwise it's not what we're looking for)
                return [num] + subs                        # Return the number and whatever come from the recursion
    return None                                            # After all that, nothing matches, return None (or null)


# In[87]:


s1 = [12, 1, 61, 5, 9, 2]
k1 = 24
k2 = 14
k3 = 75


# In[89]:


print('Given the set {} and three target sum {}, {} and {}'.format(s1, k1, k2, k3))
print('The subsets are {},{} and {}'.format(reach_target(s1, k1),
                                           reach_target(s1, k2),
                                           reach_target(s1, k3)))
print('')
print('Notice how 14 can be made up of [12, 2] and [5, 9] but because 12 was at the beginning of the list, it was accounted for first')

