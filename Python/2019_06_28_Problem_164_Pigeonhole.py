#!/usr/bin/env python
# coding: utf-8
"""2019 June 28th - Daily_Coding_Problem #164."""
# <markdown>
# ## 2019 June 28th - Daily_Coding_Problem #164
#
# This problem was asked by Google.
#
# You are given an array of length n + 1 whose elements belong to
# the set {1, 2, ..., n}. By the pigeonhole principle,
# there must be a duplicate. Find it in linear time and space.


# %%
def pigeonhole(lst):
    """Find the pigeonhole."""
    n = len(lst) - 1
    expectedSum = n*(n+1)/2
    actualSum = sum(lst)
    return actualSum - expectedSum


# %%
pigeonhole([1, 2, 3, 4, 4, 5])
