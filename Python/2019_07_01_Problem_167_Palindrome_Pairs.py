#!/usr/bin/env python
# coding: utf-8
"""2019 July 1st - Daily_Coding_Problem #167."""
# <markdown>
# ## 2019 July 1st - Daily_Coding_Problem #167
#
# This problem was asked by Airbnb.
#
# Given a list of words, find all pairs of unique indices such that
# the concatenation of the two words is a palindrome.
#
# For example, given the list ["code", "edoc", "da", "d"],
# return [(0, 1), (1, 0), (2, 3)].


# %%
def isPalindrome(string):
    """Check if the string is palindrome."""
    for i in range(len(string)//2):
        if string[i] != string[(i*-1)-1]:
            return False
    return True


def palindromePairs(lst):
    """Find all pairs of unique indices which form a palindrome."""
    results = []
    for i, e1 in enumerate(lst):
        for j, e2 in enumerate(lst):
            if i != j:
                if isPalindrome(e1+e2):
                    results.append((i, j))
    return results


# %%
palindromePairs(["code", "edoc", "da", "d"])
