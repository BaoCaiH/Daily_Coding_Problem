#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 13th
# 
# Problem: Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# 
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

# In[64]:


def run_length_encode(string):
    compare_str = ''
    result = ''
    for c in string:
        if not compare_str:
            compare_str = c
            counter = 1
        elif c == compare_str:
            counter += 1
        elif c != compare_str:
            result += str(counter) + compare_str
            compare_str = c
            counter = 1
    result += str(counter) + compare_str
    return result


# In[67]:


s1 = 'AAAABBBCCDAA'
s2 = 'AABBBUUUUTTTTTTTJJMMMFPOPPPPPK'


# In[69]:


print('Given the strings \'{}\' and \'{}\''.format(s1, s2))
print('The encoded versions are \'{}\' and \'{}\''.format(run_length_encode(s1), run_length_encode(s2)))

