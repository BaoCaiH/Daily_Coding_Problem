#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 16th
# 
# Problem: Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
# 
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
# 
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

# In[13]:


# This first function was taken from the solution of problem number 42
# Find it in my github
def reach_target(s, k):                                     # Function to get a target sum
    if len(s) == 1:                                         # If the set is only 1 element long
        if s[0] == k:                                       # If that element is the target number
            return [k]                                      # Good
        else:                                               # If not
            return None                                     # Bad
                                                            # Otherwise, real work here
    for i, num in enumerate(s):                             # For each number
        if num == k:                                        # If it's magically equal to the target
            return [num]                                    # Great
        elif num < k:                                       # Otherwise it should less than the target
            subs = reach_target(s[:i] + s[i+1:], k - num)   # Recurse the function with a subset
                                                            # without the number, and a smaller target
            if subs:                                        # If it returns anything at all
                                                            # (otherwise it's not what we're looking for)
                return [num] + subs                         # Return the number and whatever come from the recursion
    return None                                             # After all that, nothing matches, return None (or null)
                                                            #
def split_set(lst):                                         # Main function
    if sum(lst) % 2 != 0:                                   # If the sum is an odd number
        print('This multiset cannot be splited')            # Certainly this operation should not be perform
        return None                                         # Return nothing
    target = sum(lst) / 2                                   # If not then take half of the sum as the target
    set_1 = reach_target(lst, target)                       # Feed it to the function above to find the subset
    if not set_1:                                           # If the subset cannot be found
        print('This multiset cannot be splited')            # Return nothing
        return None                                         #
    set_2 = lst.copy()                                      # Get a copy of the original list
    for e in set_1:                                         # Go through the set 1
        set_2.pop(set_2.index(e))                           # Find the index and remove it from the set 2
    return (set_1, set_2)                                   # So they will become 2 subsets


# In[18]:


lst_1 = [15, 5, 20, 10, 35, 15, 10]
lst_2 = [15, 5, 20, 10, 35]
print('Given 2 sets {} and {}'.format(lst_1, lst_2))


# In[20]:


print('Set {} will have the 2 subsets {} which give the same sum'.format(lst_1, split_set(lst_1)))


# In[21]:


print('While set {} will return nothing'.format(lst_2))
split_set(lst_2)

