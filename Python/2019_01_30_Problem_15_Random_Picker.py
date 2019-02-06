#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 30th
# 
# Problem: Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

# Let's say the list has 3 elements. When the list is loop, at element i (i_max = size - 1), The rate which the element would be picked is 1/(i + 1) so that in the end the total rate would be 1/(i_max + 1). Here's why.
# 
# At the first element:
# 
# The rate of the first element is 1/1, second and third are 0
# 
# >1 : 1
# 
# >2 : 0
# 
# >3 : 0
# 
# At the second element:
# 
# The rate of the second element being picked is 1/2, the rate of the first element being not replaced, also mean picked is 1/2.
# 
# >1 : 1 * 1/2 = 1/2
# 
# >2 : 1/2
# 
# >3 : 0
# 
# At the third element:
# 
# The rate of the third element being picked is 1/3, the rate of the first and second element not being replaced, also mean picked is 2/3
# 
# >1 : 1 * 1/2 * 2/3 = 1/3
# 
# >2 : 1/2 * 2/3 = 1/3
# 
# >3 : 1/3
# 
# So in the end, the total rate will be 1/3 for each, which will be what we need

# In[21]:


def pick_random(big_list):
    import random
    random_element = None
    for index, element in enumerate(big_list): # First element, so 1/1 chance
        if index == 0:                         # From the second onward, pick a random number
            random_element = element           # and compare to a fixed number
        elif random.randint(0, index) == 0:        # The rate will move with i like the example above
            random_element = element           # But in python, the first element is counted from 0
    return random_element                      # So it looks weird, but nothing changed


# In[23]:


# This proves nothing though
# pick_random([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])


# In[18]:


print("In case you run this Python file, view with a text editor or jupyter file for explanation. Because I don't have a huge list to run an example, sorry")

