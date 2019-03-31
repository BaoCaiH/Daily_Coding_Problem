#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 31st
# 
# Problem: Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.
# 
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

# In[11]:


def longest_increasing_subsequence(array, last = None):                             #
    if not array:                                                                   # If the array is empty
        return last                                                                 # Return whatever it has
    if not last:                                                                    # This condition is to kick
        return longest_increasing_subsequence(array[1:], last = [array[0]])         # start the process
    if len(array) == 1:                                                             # If the array only has 1 item
        if array[0] > last[-1]:                                                     # Check increasing?
            return last + [array[0]]                                                # Add the last number to the
                                                                                    # subsequence if true
        else:                                                                       # Otherwise
            return last                                                             # Return whatever it has
                                                                                    # If the array is longer than 1
    if array[0] <= last[-1]:                                                        # If next number is not larger
        return longest_increasing_subsequence(array[1:], last = last)               # Skip
    else:                                                                           # If it is
        take = longest_increasing_subsequence(array[1:], last = last + [array[0]])  # There are 2 options
        skip = longest_increasing_subsequence(array[1:], last = last)               # Take it or skip
        return [take, skip][len(take) < len(skip)]                                  # Choose the longer one
                                                                                    #


# In[12]:


a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


# In[14]:


print('Given the array: {}'.format(a))


# In[16]:


print('The longest increasing subsequence is: {}'.format(longest_increasing_subsequence(a)))
print('There is more than 1 possibility, the chosen option depends on how the function is written')

