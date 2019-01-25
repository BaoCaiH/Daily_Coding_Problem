#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 25th
# 
# Problem: Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# In[12]:


def job_scheduler(func, argument, delay_time):
    import time                                # We need the built-in package time
    time.sleep(delay_time/1000)                # Just call sleep for the given milliseconds
    return func(argument)                      # And call the function


# In[14]:


def add_5(lst):
    return [i + 5 for i in lst] # For testing


# In[9]:


list_1 = [1, 2, 3, 4, 5, 6]


# In[16]:


print('Given the list {}'.format(list_1))
print('The new list will appear after roughly in 2 seconds')
job_scheduler(add_5, list_1, 2000)

