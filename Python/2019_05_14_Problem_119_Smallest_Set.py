#!/usr/bin/env python
# coding: utf-8
"""2019 May 14th - Daily_Coding_Problem #119."""
# <markdown>
# ## 2019 May 14th - Daily_Coding_Problem #119
#
# Problem: Given a set of closed intervals, find the smallest set of numbers
# that covers all the intervals. If there are multiple smallest sets,
# return any of them.
#
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9],
# one set of numbers that covers all these intervals is {3, 6}.


# %%
def smallestSet(lst):
    """Find the smallest set that covers all the given intervals."""
    left = []
    right = []
    for l, r in lst:
        left.append(l)
        right.append(r)
    return {min(right), max(left)}


# %%
a = [[0, 3], [2, 6], [3, 4], [6, 9]]
smallestSet(a)
# %%
b = [[2, 3], [3, 4], [2, 5], [5, 7], [0, 3], [2, 6], [3, 4], [6, 9]]
smallestSet(b)
