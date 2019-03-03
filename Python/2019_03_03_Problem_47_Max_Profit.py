#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 3rd
# 
# Problem: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
# 
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

# In[4]:


def max_profit(stock_levels):
    min_level = None                            # Keep track of the min stock level
    profit = 0                                  # And the profit
    for level in stock_levels:                  # For each level
        if not min_level:                       # Make sure to update the new min stock level
            min_level = level                   #
        min_level = min(level, min_level)       #
        profit = max(profit, level - min_level) # Then update the new max possible profit
    return profit                               # Return the final max profit


# In[15]:


l1 = [7, 9, 11, 8, 5, 7, 10]
l2 = [131, 123, 125, 201, 257, 199, 200]


# In[17]:


print('Given the following lists: {}, {}'.format(l1, l2))
print('The max profit respectively are {} and {}'.format(max_profit(l1), max_profit(l2)))

