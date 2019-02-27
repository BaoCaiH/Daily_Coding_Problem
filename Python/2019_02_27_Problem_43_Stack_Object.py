#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 27th
# 
# Problem: Implement a stack that has the following methods:
# 
# >push(val), which pushes an element onto the stack<br>
# >pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.<br>
# >max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# 
# Each method should run in constant time.

# In[54]:


class stack:
    def __init__(self, lst = None):               # Upon creating, we can give it a list of values
        if lst:                                   # If the values are available
            self.lst = lst                        # Store the values
        else:                                     # If not
            self.lst = []                         # Create an empty holder
            
    def push(self, val):                          # Pushing
        self.lst = self.lst + [val]               # Add the value to the holder
    
    def pop(self):                                # Popping
        if self.lst:                              # If the holder is not empty
            last = self.lst[-1]                   # Get the last
            self.lst = self.lst[:-1]              # Remove the last element
            return last                           # Return the last
        else:                                     # Else, Error and None
            print('Error, the stack is empty')
            return None
        
    def max(self):                                # Max
        if self.lst:                              # If there is something
            return max(self.lst)                  # Return the max
        else:                                     # Else, Error and None
            print('Error, the stack is empty')
            return None


# In[2]:


a = [1, 2, 3,4, 5]


# In[47]:


b = stack([1, 2, 5, -2])


# In[48]:


b.push(3)


# In[53]:


b.max()

