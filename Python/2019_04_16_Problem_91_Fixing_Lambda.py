#!/usr/bin/env python
# coding: utf-8

# ### 2019 April 16th
# 
# Problem: What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
# 
# `functions = []
# for i in range(10):
#     functions.append(lambda : i)
# for f in functions:
#     print(f())`

# In[42]:


functions = []
for i in range(10):
    functions.append(lambda : i)

i = 0
for f in functions:
    print(f())
    i += 1

