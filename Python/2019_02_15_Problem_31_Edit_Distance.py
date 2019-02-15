#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 15th
# 
# Problem: The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
# 
# Given two strings, compute the edit distance between them.

# In[20]:


def edit_distance(string_1, string_2):
    remain = ''
    for c in string_1:
        if c in string_2:
            i = string_2.index(c)
            string_2 = string_2[:i] + string_2[i+1:]
        else:
            remain += c
    return max(len(remain), len(string_2))


# In[18]:


s1 = 'kitten'
s2 = 'sitting'
s3 = 'mitten'
s4 = 'substitute'
s5 = 'statue'


# In[24]:


print('Two strings \'{}\' and \'{}\' have edit distance of {}'.format(s1, s2, edit_distance(s1, s2)))
print('Two strings \'{}\' and \'{}\' have edit distance of {}'.format(s1, s3, edit_distance(s1, s3)))
print('Two strings \'{}\' and \'{}\' have edit distance of {}'.format(s4, s5, edit_distance(s4, s5)))


# In[ ]:




