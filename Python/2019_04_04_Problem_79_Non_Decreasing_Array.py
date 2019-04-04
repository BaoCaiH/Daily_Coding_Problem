#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 4th
# 
# Problem: Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
# 
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
# 
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

# In[2]:


def non_decreasing(array):                          #
    if len(array) <= 2:                             # If there are 2 or less element, it is naturally descending
        return True                                 # Or changable, because, you know...
    holder = []                                     #
    counter = 0                                     # Counter for the "tipping point"
    for e in array:                                 # Search each element
        holder.append(e)                            # Put it in the holder
        if len(holder) == 2:                        # From the second element
            if holder[-1] <= holder[-2]:            # If the trend is decreasing at this point
                counter += 1                        # Add 1 to the counter
        elif len(holder) >= 3:                      # From the third
            if holder[-1] <= holder[-2]:            # If it's still decreasing
                if holder[-1] - holder[-3] >= 2:    # and if current element is at least 2 unit larger than the
                    counter += 1                    # third last element, then add 1 to the counter
                else:                               # But if not
                    return False                    # Then it is not changable
        if counter > 1:                             # After each element, if the counter is more than 1
            return False                            # Return False
    return True                                     # After all, return True


# In[6]:


l1 = [10, 5, 7]
l2 = [10, 5, 1]
l3 = [10, 5, 7, 9, 10, 11, 14]
l4 = [10, 5, 7, 9, 6, 12, 14]
l5 = [1, 3, 5, 10, 7, 9, 11]


# In[16]:


print('Given 5 different array: {}'.format(l1))
print('                         {}'.format(l2))
print('                         {}'.format(l3))
print('                         {}'.format(l4))
print('                         {}'.format(l5))


# In[18]:


print('The results are {}, {}, {}, {} and {} respectively to whether the arrays can become non-decreasing'.format(
non_decreasing(l1), non_decreasing(l2), non_decreasing(l3), non_decreasing(l4), non_decreasing(l5)))

