#!/usr/bin/env python
# coding: utf-8
"""2019 June 23rd - Daily_Coding_Problem #159."""
# <markdown>
# ## 2019 June 23rd - Daily_Coding_Problem #159
#
# This problem was asked by Google.
#
# Given a string, return the first recurring character in it,
# or null if there is no recurring chracter.
#
# For example, given the string "acbbac", return "b".
# Given the string "abcdef", return null.


# %%
def firstRecurringChar(txt):
    """Return the first recurring character."""
    listing = []
    for c in txt:
        if c in listing:
            return c
        listing.append(c)
    return None


# %%
txt = 'abcdef'
firstRecurringChar(txt)
