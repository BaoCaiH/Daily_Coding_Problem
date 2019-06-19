#!/usr/bin/env python
# coding: utf-8
"""2019 June 19th - Daily_Coding_Problem #155."""
# <markdown>
# ## 2019 June 19th - Daily_Coding_Problem #155
#
# This problem was asked by MongoDB.
#
# Given a list of elements, find the majority element,
# which appears more than half the time (> floor(len(lst) / 2.0)).
#
# You can assume that such element exists.
#
# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.


# %%
def majorityElement(lst):
    """Find the element which appear more than half of the time."""
    elementDict = {}
    for e in lst:
        if e not in elementDict:
            elementDict[e] = 0
        elementDict[e] += 1

    halfTime = len(lst) // 2
    for e, occurence in elementDict.items():
        if occurence > halfTime:
            return e
    return None


# %%
majorityElement([1, 2, 1, 1, 3, 4, 1, 1])
