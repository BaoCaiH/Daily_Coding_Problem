#!/usr/bin/env python
# coding: utf-8
"""2019 June 29th - Daily_Coding_Problem #165."""
# <markdown>
# ## 2019 June 29th - Daily_Coding_Problem #165
#
# This problem was asked by Google.
#
# Given an array of integers,
# return a new array where each element in the new array is
# the number of smaller elements to the right of that element in
# the original input array.
#
# For example, given the array `[3, 4, 9, 6, 1]`,
# return `[1, 1, 2, 1, 0]`, since:
#
# There is 1 smaller element to the right of 3
#
# There is 1 smaller element to the right of 4
#
# There are 2 smaller elements to the right of 9
#
# There is 1 smaller element to the right of 6
#
# There are no smaller elements to the right of 1


# %%
def smallerElements(lst):
    """Return the number of smaller elements to the right of each element."""
    smallerLst = []
    for i in range(len(lst)):
        smaller = 0
        for e in lst[i+1:]:
            if lst[i] > e:
                smaller += 1
        smallerLst.append(smaller)
    return smallerLst


# %%
smallerElements([3, 4, 9, 6, 1])
