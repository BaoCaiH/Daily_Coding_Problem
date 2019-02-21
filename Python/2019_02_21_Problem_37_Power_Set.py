#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 21st
# 
# Problem: The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# 
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# 
# You may also use a list or array to represent a set.

# In[76]:


def power_set(sets):
    power = [[]]                              # This is the prequisite, there's always an empty subset
    for element in sets:                      # For each element
        for sub in power:                     # Iter the power set so far
            power = power + [sub + [element]] # Add the new element to each subset so far to be the new subset
            # I tried power.append(sub.append(element))
            # But it's not working
            # Instead, it has to be broken down into:
            # sub.append(element)
            # power.append(sub)
            # This is quite longer
            # And it seems not working either
    return power


# In[3]:


l1 = [1, 2, 3, 4]


# In[78]:


print('Given the set {}'.format(l1))
print('Here is the power set:')
print(power_set(l1))

