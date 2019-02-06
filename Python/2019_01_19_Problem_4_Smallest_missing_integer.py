#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 19th
# 
# Problem: Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# 
# You can modify the input array in-place.

# In[3]:


def smallest_missing_integer(array_or_list):
    import numpy as np                                        # This function need numpy
    array = np.array(array_or_list)                           # We neen the characteristic of numpy array
    array.sort()                                              # Sort it ascending so we know when it turn from negative to positive
    print('The given array was {}'.format(array))             # This is just for fun
    compare_array = [0]                                       # Create a compare array, to compare the 2 adjacent numbers
    for i in range(len(array) - 1):                           # There's probably a better way
        compare_array.append(array[i])
    compare_array = np.array(compare_array)
#     print(compare_array)
    compared = array - compare_array                          # The comparison is here, we will have an array of the differences between 2 adjacent numbers
    for j in range(len(compared)):
        if (compared[j] > 1 and array[j] > 0):                # If the difference is greater than 1, there should be something in between, and if the later is positive then the in-between might be positive too
            for k in range(compare_array[j], (array[j] + 1)): # So wo loop through the gap
                if k > 0 and (k not in array):                # If anything in the gap is not in the array, and is positive
                    print('The smallest missing integer was {}'.format(k))
                    return k                                  # That's the missing number and stop the function right there


# In[4]:


smallest_missing_integer([1, 2, -1, 5, 5, 6, -4, 2, 45, 1, 6, 3]) # Mayhemmmm

