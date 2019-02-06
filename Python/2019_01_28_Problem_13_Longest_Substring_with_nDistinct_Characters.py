#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 28th
# 
# Problem: Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# 
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

# In[32]:


s = 'aaabcbccatr'
k = 2


# In[27]:


def longest_substring(s, k):
    def unique_characters(string):             # A separate function to count the number of unique character
        nunique = []                           # This list is to store the unique characters
        for s in string:
            if s not in nunique:               # If not already exist in list, then append
                nunique.append(s)
        return len(nunique)
    def iterate_string(string):                # Go over the string
        subs = []                              # A list to store the current char which fits the k distinct
        longest_subs = []                      # A list to store the longest set of chars with k distinct
        for char in string:
            subs.append(char)                  # Add the new char into the holder
            while unique_characters(subs) > k: # Then delete the pre-char until it fits the k distinct
                subs = subs[1:]
            if len(subs) > len(longest_subs):  # If the current holder is longer than the current longest
                longest_subs = subs.copy()     # Change
        return ''.join(longest_subs)           # Join the characters
    return iterate_string(s)


# In[33]:


print('The initial string is \'{}\' and with \'{}\' distinct characters, and the longest substring is \'{}\''.format(s, k, longest_substring(s, k)))


# In[34]:


s = input('Give your own string: ')
k = int(input('Give your own number of distinct characters: '))
print('The longest substring is {}'.format(longest_substring(s, k)))

