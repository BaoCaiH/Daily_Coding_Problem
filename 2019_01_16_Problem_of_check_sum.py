#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 16th
# 
# Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# In[8]:


def sum_any_two_numbers_in_list_equal(list, check_total):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i] + list[j]) == check_total:
                return True
    return False


# In[11]:


l = [10, 15, 3, 7, 3, 7, 9, 1, 10]
k = 14

print('The list is ', end = '')
print(l)
print('The check number is ', end = '')
print(k)

# In[12]:

print('Is there sum of any two number in the list equal to the check number ')
print(sum_any_two_numbers_in_list_equal(l, k))

