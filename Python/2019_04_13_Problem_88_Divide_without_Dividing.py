#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 13th
# 
# Problem: Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

# In[7]:


def aDivB(a, b):
    quo = 0
    while a >= b:
        quo += 1
        a -= b
    return quo, a


# In[8]:


a = int(input('a is '))
b = int(input('b is '))
quo, rem = aDivB(a, b)
print('{} divided by {} is {} with {} remainder'.format(a, b, quo, rem))

