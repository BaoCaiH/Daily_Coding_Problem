#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 22nd
# 
# Problem: Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.
# 
# Write a function to simulate an unbiased coin toss.

# In[8]:


# Assume??? ASSUME???
# That's not how we do things here
# We'll make it
def toss_biassed(bias = 0.7):                   #
    import random                               #
    return 1 if random.random() > 0.7 else 0    # Return result according to the bias

# Now let's make it unbias
def unbias():                                   #
    roll_1 = toss_biassed()                     # Roll the biased coin twice
    roll_2 = toss_biassed()                     # The probabilities of the combined rolls will always be
    if roll_1 == 1 and roll_2 == 0:             # r(1 - r)
        return 1                                # So it would be fair and unbias
    elif roll_1 == 0 and roll_2 == 1:           #
        return 0                                #
    else:                                       # Any other combination will cause a re-roll
        return unbias()                         #


# In[20]:


unbias()

