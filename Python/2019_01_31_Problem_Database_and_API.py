#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 31st
# 
# Problem: You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
# 
# record(order_id): adds the order_id to the log
# 
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# 
# You should be as efficient with time and space as possible.

# In[96]:


class id_log:
    def __init__(self, N):
        self.revolver = [None] * N                                               # Store N last items
        self.index = 0                                                           # Track where the item is
    
    def record(self, order_id):
        self.revolver[self.index] = order_id                                     # Record in the next position
        self.index += 1                                                          # Increase by 1 position
        if self.index == len(self.revolver):                                     # When the list is full
            self.index = 0                                                       # Turn back to the first position
    
    def get_last(self, i):
        if self.index > i:                                                       # If the i is less than the position
            return self.revolver[(self.index - i):self.index]                    # return anything in between
        elif self.index == i:                                                    # If they are the same
            return self.revolver[:self.index]                                    # return from start to the position
        else:                                                                    # Else
            return self.revolver[:self.index] + self.revolver[(self.index - i):] # return from start and the last few positions


# In[100]:


log = id_log(8)
for i in range(30):
    log.record(i)


# In[101]:


log.get_last(8)


# In[102]:


log.record(1)
log.get_last(1)


# In[103]:


log.get_last(2)


# In[104]:


log.get_last(3)


# In[105]:


log.get_last(4)


# In[106]:


log.get_last(5)


# In[107]:


log.get_last(6)


# In[108]:


log.get_last(7)


# In[109]:


log.get_last(8)

