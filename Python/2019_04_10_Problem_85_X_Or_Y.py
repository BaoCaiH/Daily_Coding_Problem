#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 10th
# 
# Problem: Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

# In[31]:


# If b = 1, the equation becomes x*1 - y*0 = x
# If b = 0, the equation becomes x*0 - y*(-1) = y
def xOrY(x, y, b):
#     return x*bool(b) - y*(bool(b)-1)
    return x*b - y*(b-1) 


# In[35]:


xOrY(19, 4, 0)

