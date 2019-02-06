#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 4th
# 
# Problem: Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# 
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# 
# In this example, assume nodes with the same value are the exact same node objects.
# 
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

# In[1]:


a = [3, 7, 8, 10]
b = [99, 1, 8, 10]


# In[4]:


def intersections(lst1, lst2):
    node = []
    for e1 in lst1:
        if len(node) == 1:
            return node
        if e1 in lst2 and e1 not in node:
            node.append(e1)
    return node


# In[6]:


print('Given list a - {} and list b - {}'.format(a, b))
print('The intersect node is {}'.format(intersections(a, b)))


# In[7]:


c = input('Input list c (i.e.: 1,3,4,7,8) ')
c = c.split(',')
d = input('Input list d (i.e.: 1,3,4,7,8) ')
d = d.split(',')
print('The intersect node is {}'.format(intersections(c, d)))

