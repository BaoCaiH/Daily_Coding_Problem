#!/usr/bin/env python
# coding: utf-8
"""2019 May 16th - Daily_Coding_Problem #121."""
# <markdown>
# ## 2019 May 16th - Daily_Coding_Problem #121
#
# Problem: Given a string which we can delete at most k,
# return whether you can make a palindrome.
#
# For example, given 'waterrfetawx' and a k of 2,
# you could delete f and x to get 'waterretaw'.


# %%


def makePalindrome(string, k):
    """Check if removing at most k characters to make it palindrome."""
    reverseStr = ''.join([string[i] for i in range(len(string)-1, -1, -1)])
    length = len(string)
    offset = 0
    for i in range(length):
        for j in range(i+offset, length):
            if string[i] == reverseStr[j]:
                offset = j - i
                break
        if offset > k:
            return False
    return True


# %%
s = 'waterrfetawx'
k = 2
# %%
makePalindrome(s, k)
# %%
