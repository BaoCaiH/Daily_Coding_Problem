#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 14th
# 
# Problem: An sorted array of integers was rotated an unknown number of times.
# 
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
# 
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
# 
# You can assume all the integers in the array are unique.

# In[20]:


def indexing(lst, k):                                               #
    if k == lst[0]:                                                 # If the first element match
        return 0                                                    # Lucky
    elif k > lst[0]:                                                # If the first is larger than the objective
        for i, e in enumerate(lst):                                 # Move forward from the front
            if lst[i-1] > e:                                        # If the rate of change, changes sign
                print('The element does not exist in the array')    # and we haven't found a match
                return None                                         # Yeah it's over
            if e == k:                                              # Then when found
                return i                                            # Return the index
            elif e > k:                                             # If the number is larger than onjective
                print('The element does not exist in the array')    # Means the objective is not in the array
                return None                                         #
    else:                                                           # If the first is less than the objective
        length = len(lst)                                           # Move backward
        for i in range(length - 1, 0, -1):                          # With the largest index first
            if lst[i] == k:                                         # If found
                return i                                            # Return
            elif lst[i] < k:                                        # If not
                print('The element does not exist in the array')    # Throw error
                return None                                         #
            if lst[i-1] < lst[i]:                                   # Because of indexing algorithm
                print('The element does not exist in the array')    # This has to be done at the end
                return None                                         # So that the index won't be out of range


# In[12]:


lst = [13, 18, 25, 2, 8, 10]
print('Given the array: {}'.format(lst))


# In[21]:


k = int(input('Please choose a number to find, it can be something not in the array, to see the effect: '))
indexing(lst, k)

