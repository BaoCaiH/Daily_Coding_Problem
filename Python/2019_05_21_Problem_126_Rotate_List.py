#!/usr/bin/env python
# coding: utf-8
"""2019 May 21st - Daily_Coding_Problem #126."""
# <markdown>
# ## 2019 May 21st - Daily_Coding_Problem #126
#
# Problem: Write a function that rotates a list by k elements.
# For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list.
# How many swap or move operations do you need?


# %%
def rotateList(lst, k):
    """Rotate a list by k elements."""
    return lst[k % len(lst):] + lst[:k % len(lst)]


# %%
rotateList([1, 2, 3, 4, 5, 6], 8)
