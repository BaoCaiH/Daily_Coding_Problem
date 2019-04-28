#!/usr/bin/env python
# coding: utf-8
"""2019 April 28th - Daily_Coding_Problem #103."""
# <markdown>
# ## 2019 April 28th - Daily_Coding_Problem #103
#
# Problem: Given a string and a set of characters,
# return the shortest substring containing all the characters in the set.
#
# For example, given the string "figehaeci" and
# the set of characters {a, e, i}, you should return "aeci".
#
# If there is no substring containing all the characters in the set,
# return null.


# <codecell>
def shortestSubstring(string, charSet):
    """
    Return the shortest substring.

    The substring shall contain all the characters in a given set.
    """
    subStrings = []
    for i, firstChar in enumerate(string):
        if firstChar in charSet:
            subset = [firstChar]
            for char in string[i+1:]:
                subset.append(char)
                if all(c in subset for c in charSet):
                    subStrings.append(''.join(subset))
                    break
    if not subStrings:
        return None
    minLength = min([len(sub) for sub in subStrings])
    return min(filter(lambda x: len(x) == minLength, subStrings))


# %%
string = "figehaeci"
set = ['a', 'e', 'i']
shortestSubstring(string, set)
