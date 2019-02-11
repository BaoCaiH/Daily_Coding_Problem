#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 11th
# 
# Problem: Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# 
# For example, given the string "([])\[\]({})", you should return true.
# 
# Given the string "([)]" or "((()", you should return false.

# In[18]:


def is_balance(brackets):
    string = brackets
    while string:
        original_length = len(string)
        for i in range(original_length - 1):
            if string[i:i+2] in ['()', '[]', '{}']:
                string = string[:i] + string[i+2:]
                break
        if len(string) == original_length:
            return False
    return True


# In[24]:


s1 = '()'
s2 = '([])[]({})'
s3 = "([)]"
s4 = "((()"


# In[27]:


print('Given the 4 bracket sets: \'{}\', \'{}\', \'{}\' and \'{}\''.format(s1, s2, s3, s4))
print('The results are as follow: {}, {}, {} and {}'.format(is_balance(s1), is_balance(s2), is_balance(s3), is_balance(s4)))

