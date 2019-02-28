#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 28th
# 
# Problem: We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
# 
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
# 
# You may assume each element in the array is distinct.
# 
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

# In[66]:


def inversions(lst):
    inverse = []
    for i, e in enumerate(lst[:-1]):    # For each number
        for f in lst[i+1:]:             # Compare to the rest
            if e > f:                   # If it the condition meet (condition above)
                inverse.append((e, f))  # Add it
    return inverse


# In[2]:


l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 1, 3, 5]
l3 = [5, 4, 3, 2, 1]


# In[89]:


print(l1)
print(inversions(l1))
print(l2)
print(inversions(l2))
print(l3)
print(inversions(l3))

