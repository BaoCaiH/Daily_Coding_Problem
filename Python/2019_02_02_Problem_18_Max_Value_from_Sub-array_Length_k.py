#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 2nd
# 
# Problem: Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
# 
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 
# 10 = max(10, 5, 2)
# 
# 7 = max(5, 2, 7)
# 
# 8 = max(2, 7, 8)
# 
# 8 = max(7, 8, 7)
# 
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

# In[19]:


ar1 = [10, 5, 2, 7, 8, 7]
k1 = 3


# In[7]:


def max_val_from_sub_k(array, k):
    count = len(array) - k
    max_val = []
    for i in range(0, count + 1):
        max_val.append(max(array[i : i + k]))
    return max_val


# In[20]:


print('Given the array {} and k of {}'.format(ar1, k1))
print('Return the max values set {}'.format(max_val_from_sub_k(ar1, k1)))


# In[21]:


ar2 = input('Give your own array of numbers separated by comma (i.e 1,2,3): ')
ar2 = ar2.split(',')
ar2 = [int(i) for i in ar2]
print(ar2)
k2 = int(input('Give your own k: '))
print('Return the max values set {}'.format(max_val_from_sub_k(ar2, k2)))

