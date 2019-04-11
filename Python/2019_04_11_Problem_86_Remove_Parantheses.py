#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 11th
# 
# Problem: Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
# 
# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

# In[9]:


def removeParantheses(string):
    # Empty string does not need any removal
    if not string:
        return 0
    
    # If there is no pairs, everything must be removed
    if '()' not in string:
        return len(string)
    
    # Otherwise, take the lesser of remove the pair or search both sides of the pair
    ind = string.index('()')
    return min((removeParantheses(string[:ind]) + removeParantheses(string[ind+2:])),
              removeParantheses(string[:ind] + string[ind+2:]))


# In[11]:


s1 = '()())()'
s2 = ')('
s3 = '(())))(()'


# In[14]:


print('The string "{}" has {} parantheses that need to be removed'.format(s1, removeParantheses(s1)))
print('The string "{}" has {} parantheses that need to be removed'.format(s2, removeParantheses(s2)))
print('The string "{}" has {} parantheses that need to be removed'.format(s3, removeParantheses(s3)))

