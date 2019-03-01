#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 1st
# 
# Problem: Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

# In[41]:


def rand5():                            # Apparently python does not have a built-in rand5()
    import random                       # Still need random
    element = None                      # Create a holder
    for i in range(1, 6):               # For 5 times
        if i == 1:                      # First, give number '1' a starting probability of 100%
            element = i
        elif random.randint(1, i) == 1: # Then gradually decreasing it while increase other elements' probs
            element = i
    return element                      # Find the math in Problem_15_Random_Picker


# In[42]:


def rand7():                    # Since rand5() is already uniform
    i = 5*rand5() + rand5() - 5 # This expression using rand5() twice to create a range of number from 1 to 25
    if i < 22:                  # We only use those less than 21 (FYI, a multiple of 7)
        return i % 7 + 1        # Take the remainder after divided by 7, ranging from 0 to 6, so add 1
    return rand7()              # Otherwise make it choose another number


# In[52]:


rand7()

