#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 19th
# 
# Problem: Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
# 
# Do this in linear time and in-place.
# 
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

# In[1]:


def rgb(array):
    for i, e in enumerate(array):                                   # For each index and element in the array
        for j in range(i, 0, -1):                                   # Compare it to the previous elements
            if e == 'R':                                            # If the element is 'R'
                if array[j - 1] == 'R':                             # And the previous is also 'R'
                    break                                           # It's at the right place
                else:                                               # Else, swap to move up and continue
                    array[j], array[j - 1] = array[j - 1], array[j]
            if e == 'G':                                            # If the element is 'G'
                if array[j - 1] == 'B':                             # And the previous is 'B'
                    array[j], array[j - 1] = array[j - 1], array[j] # Swap to move up
                else:                                               # Else, it is either at the 'G's place
                    break                                           # or behind a 'R', it's all good
                                                                    # 'B' doesn't need to go anywhere
                                                                    # just be at the last


# In[2]:


c1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
c2 = ['B', 'G', 'B', 'R', 'B', 'B', 'R', 'R', 'R', 'G']


# In[3]:


print('The first array is {}'.format(c1))
rgb(c1)
print('And after swapping: {}'.format(c1))
print('')
print('The second array is {}'.format(c2))
rgb(c2)
print('And after swapping: {}'.format(c2))

