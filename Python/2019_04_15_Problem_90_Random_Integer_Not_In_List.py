#!/usr/bin/env python
# coding: utf-8

# ### 2019 April 15th
# 
# Problem: Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

# In[24]:


def randomIntegerNotInList(n, l):
    from random import randint
#     for i in range(n):
#         if i == 0:
#             integer = i
#         elif randint(0, i) == 0:
#             integer = i
    integer = randint(0, n - 1)
    if integer in l:
        return randomIntegerNotInList(n, l)
    return integer


# In[25]:


n = 10000
l = [1, 3, 9]


# In[130]:


randomIntegerNotInList(n, l)

