#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 17th
# 
# Problem: Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# 
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# 
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 
# 2<br>
# 1.5<br>
# 2<br>
# 3.5<br>
# 2<br>
# 2<br>
# 2

# In[90]:


def print_median(lst):                                 # Numpy can do this nicely but that's not why I'm here
    print_lst = []                                     # Empty list
    counter = 0                                        # Counter so no need for count sort
    for e in lst:                                      # Add each element to the empty list
        print_lst.append(e)
        counter += 1                                   # Add the counter as well
        print_lst.sort()                               # Sort it
        if counter % 2 == 0:                           # Print the avg between 2 middle numbers
            print((print_lst[counter // 2] +                   print_lst[(counter // 2) - 1]) / 2)
        else:
            print(print_lst[counter // 2])             # Print the middle number


# In[23]:


l1 = [1, 34, 6, 8, 0, 6, 23]
l2 = [2, 1, 5, 7, 2, 0, 5]


# In[91]:


print('Given the list {} and the results is below:'.format(l1))
print_median(l1)
print('Given the list {} and the results is below:'.format(l2))
print_median(l2)

