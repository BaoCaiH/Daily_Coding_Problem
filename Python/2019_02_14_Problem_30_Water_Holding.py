#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 14th
# 
# Problem: You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
# 
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# 
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# 
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

# In[2]:


def water_holding(walls):
    hollows = 0                                     # Count the actual space that hold water
    water = 0                                       # Count unit water
    for i, wall in enumerate(walls):
        if i == 0:                                  # If this is the first wall it cannot hold water
            holder = wall                           # It would be the first holder
        elif i == len(walls) - 1:                   # If it's the last one, same thing
            if wall < holder:                       # Also if this wall is shorter, 
                water -= (holder - wall) * hollows  # Water will flow out
        else:                                       # Otherwise
            if wall < holder:                       # If the wall is shorter
                water += holder - wall              # Fill water
                hollows += 1                        # Count the space
            else:                                   # If it's higher
                holder = wall                       # Change the holder
                hollows = 0                         # Recount
    return water


# In[8]:


w1 = [2, 1, 2]
w2 = [3, 0, 1, 3, 0, 5]
w3 = [5, 3, 2, 0, 5, 0, 1, 3]
w4 = [3, 1, 0, 5, 0, 2, 3, 5]


# In[7]:


print('Given 3 different layouts {}, {} and {}'.format(w1, w2, w3))
print('These layout can hold {}, {} and {} unit of water respectively'.format(water_holding(w1), water_holding(w2), water_holding(w3)))


# In[ ]:




