#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 24th
# 
# Problem: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# 
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# 
# Follow-up: Can you do this in O(N) time and constant space?

# In[66]:


list_1 = [2, 4, 6, 2, 5]
list_2 = [5, 1, 1, 5]
list_3 = [3, 6, 9, 6, 4, 9, -7, -8]
list_4 = [3, 6, 9, 6, 0, 0, 4, 9, 0, 0]


# In[64]:


def largest_sum_non_adjacent(lst):
    
    if len(lst) == 0:                                            # If the list is empty, largest value is 0
        return 0
    elif len(lst) <= 2:                                          # If the list only have 1 or 2 elements
        return max(max(lst), 0)                                          # Pick which ever is larger among 2 (or 1)
    elif len(lst) == 3:                                          # If there are 3, either the middle number
        return max((lst[0] + lst[2]), lst[1], 0)                 # or the sum of the outsider would be the largest
    else:                                                        # Otherwise, for every 2 adjacent numbers
        return max((lst[0] + largest_sum_non_adjacent(lst[2:])), # Compare the sum of each number
                   lst[1] + largest_sum_non_adjacent(lst[3:]),   # with the results of the same function
                   0 + largest_sum_non_adjacent(lst[1:]),         # iterate over the remaining of the list
                   0 + largest_sum_non_adjacent(lst[2:]))         # account also any negative numbers
                                                                 # they should simply be skipped


# In[67]:


print('Given the 4 lists')
print('List 1:')
print(list_1)
print('The largest sum of non-adjacent numbers is: {}'.format(largest_sum_non_adjacent(list_1)))
print('List 2:')
print(list_2)
print('The largest sum of non-adjacent numbers is: {}'.format(largest_sum_non_adjacent(list_2)))
print('List 3:')
print(list_3)
print('The largest sum of non-adjacent numbers is: {}'.format(largest_sum_non_adjacent(list_3)))
print('List 4:')
print(list_4)
print('The largest sum of non-adjacent numbers is: {}'.format(largest_sum_non_adjacent(list_4)))


# In[72]:


print('To be fair, you can give your own list of number in the form of numbers separated by spaces')
print('i.e: 3 6 9 6 0 0 4 9 0 0')
print('Errors will occur so check your syntax before confirm by press Enter')


# In[68]:


list_5 = input('Input here: ')


# In[70]:


list_5 = [int(i) for i in list_5.split(' ')]


# In[71]:


print('The largest sum of non-adjacent numbers is: {}'.format(largest_sum_non_adjacent(list_5)))

