#!/usr/bin/env python
# coding: utf-8
"""2019 May 6th - Daily_Coding_Problem #111."""
# <markdown>
# ## 2019 May 6th - Daily_Coding_Problem #111
#
# Problem: Given a word W and a string S,
# find all starting indices in S which are anagrams of W.
#
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


# %%
def anagrams(w, s):
    """Find all starting anagram positions."""
    def isAnagrams(w1, w2):
        for c in w1:
            try:
                i = w2.index(c)
                w2 = w2[:i] + w2[i+1:]
            except ValueError:
                return False
        return True
    length = len(w)
    positions = []
    for i, c in enumerate(s):
        if c in w:
            if isAnagrams(w, s[i:i+length]):
                positions.append(i)
    return positions


# %%
w = 'abc'
s = 'acbxacbabiunbaoicba'
anagrams(w, s)
