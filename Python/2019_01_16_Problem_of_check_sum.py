#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 16th
# 
# Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# In[12]:


def sum_any_two_numbers_in_list_equal(list, check_total):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i] + list[j]) == check_total:
                print('The sum of number {} at position {} and number {} at position {} equal {}'.                      format(list[i], i, list[j], j, check_total))
                return True
    print('There is no sum of two number equal {}'.format(check_total))
    return False


# In[3]:


l = [10, 15, 3, 7, 3, 7, 9, 1, 10]
k = 14


# In[4]:


print('The list is ', end = '')
print(l)
print('The check number is ', end = '')
print(k)


# In[13]:


print(sum_any_two_numbers_in_list_equal(l, k))

