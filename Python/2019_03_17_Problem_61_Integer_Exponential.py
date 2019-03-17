#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 17th
# 
# Problem: Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
# 
# Do this faster than the naive method of repeated multiplication.
# 
# For example, pow(2, 10) should return 1024.

# In[14]:


def power(x, y):                            #
    if y == 0:                              # If the power is 0
        return 1                            # The exponential is 1
    elif y > 0:                             # If the power is positive
        if y % 2 != 0:                      # And the power is odd
            return x * power(x, y - 1)      # Recurse with 1 less unit power
        elif y % 2 == 0:                    # If the power is even
            return power(x * x, y // 2)     # Recurse with the number squared and half the power
    else:                                   # If the power is negative
        if y % 2 != 0:                      # And is odd
            return (1/x) * power(x, y + 1)  # Recurse with 1 more unit power, this time, with division
        elif y % 2 == 0:                    # If the power is even
            return power((1/(x*x)), y // 2) # Recurse with 1 divided by the number squared and half the power


# In[15]:


x = int(input('Please give an "x" number, it can be negative: '))
y = int(input('Please give a "y" number, this one cannot be negative: '))
print('{} power {} is {}'.format(x, y, power(x, y)))

