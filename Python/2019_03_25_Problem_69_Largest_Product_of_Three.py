#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 25th
# 
# Problem: Given a list of integers, return the largest product that can be made by multiplying any three integers.
# 
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# In[25]:


def largest_product_of_three(lst):                      #
    largest = None                                      # Largest number for preference
    combination = []                                    # Combination holder
    for i, num_1 in enumerate(lst[:-2]):                # A 3 layers nested loop
        for j, num_2 in enumerate(lst[i + 1 : -1]):     # To search for a combination of 3 numbers
            for k, num_3 in enumerate(lst[j + 1 :]):    #
                if not largest:                         # If none of the combination was recorded
                    combination = [num_1, num_2, num_3] # Well, record it
                    largest = num_1 * num_2 * num_3     #
                elif num_1 * num_2 * num_3 > largest:   # If yes then compared with the recorded
                    combination = [num_1, num_2, num_3] # Then replace if needed
                    largest = num_1 * num_2 * num_3     #
    return largest, combination                         #


# In[2]:


import random


# In[10]:


a = [random.randint(-10, 10) for _ in range(random.randint(4, 10))]


# In[16]:


print('This list of number is randomly generated each time this program is run, both length and elements: {}'.format(a))


# In[23]:


p, l = largest_product_of_three(a)
print('And the largest product of 3 numbers is {} by multiplying {}'.format(p, l))

