#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 1st
# 
# Problem: You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.
# 
# For example, given the following table:
# 
# cba<br>
# daf<br>
# ghi
# 
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:
# 
# ca<br>
# df<br>
# gi
# 
# So your function should return 1, since we only needed to remove 1 column.
# 
# As another example, given the following table:
# 
# abcdef
# 
# Your function should return 0, since the rows are already ordered (there's only one row).
# 
# As another example, given the following table:
# 
# zyx<br>
# wvu<br>
# tsr
# 
# Your function should return 3, since we would need to remove all the columns to order it.

# In[5]:


def columnsToRemove(lst):                   #
    length = len(lst)                       #
    if length <= 1:                         # If there is only 1 row, it is already lexicography ordered
        return 0                            #
    columnIndexes = []                      #
    for col in range(len(lst[0])):          # Search by column
        ref = ''                            # '' is always the smallest lexicography element
        for row in range(length):           # Then move row by row
            if lst[row][col] > ref:         # If the current element is larger than the previous element
                ref = lst[row][col]         # Move on
            else:                           # Otherwise
                columnIndexes.append(col)   # Add the column index to the list
                break                       # Break the second loop
    return len(columnIndexes)               # Return the length of the list


# In[1]:


l1 = ['cba', 'daf', 'ghi']
l2 = ['abcdef']
l3 = ['zyx', 'wvu', 'tsr']


# In[13]:


print('Given the 3 matrix:')
for r in l1:
    print(r)
print('')
for r in l2:
    print(r)
print('')
for r in l3:
    print(r)
print('')


# In[14]:


print('The number of columns to remove for each matrix respectively are {}, {} and {}'.format(
columnsToRemove(l1), columnsToRemove(l2), columnsToRemove(l3)))

