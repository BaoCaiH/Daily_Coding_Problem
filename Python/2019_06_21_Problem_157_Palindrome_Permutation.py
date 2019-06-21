#!/usr/bin/env python
# coding: utf-8
"""2019 June 21st - Daily_Coding_Problem #157."""
# <markdown>
# ## 2019 June 21st - Daily_Coding_Problem #157
#
# This problem was asked by Amazon.
#
# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, `carrace` should return `true`, since it can be rearranged
# to form `racecar`, which is a palindrome. `daily` should return `false`,
# since there's no rearrangement that can form a palindrome.


# %%
def palindromePermutation(txt):
    """Return if the text has a permutation which is a palindrome."""
    leftover = []
    for c in txt:
        if c not in leftover:
            leftover.append(c)
        else:
            leftover.pop(leftover.index(c))
    if len(leftover) > 1:
        return False
    return True


# %%
txt = 'daily'
palindromePermutation(txt)
