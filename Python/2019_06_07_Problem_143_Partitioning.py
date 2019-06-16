#!/usr/bin/env python
# coding: utf-8
"""2019 June 7th - Daily_Coding_Problem #143."""
# <markdown>
# ## 2019 June 7th - Daily_Coding_Problem #143
#
# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
# The first part contains all elements in lst that are less than x
#
# The second part contains all elements in lst that are equal to x
#
# The third part contains all elements in lst that are larger than x
#
# Ordering within a part can be arbitrary.
#
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10],
# one partition may be [9, 3, 5, 10, 10, 12, 14].


# %%
def partitioning(x, lst):
    """Partition the list into 3 parts."""
    partition = []
    stack = {0: 0, 1: 0, 2: 0}
    for e in lst:
        if e < x:
            partition = partition[:stack[0]] + [e] + partition[stack[0]:]
            stack[0] += 1
            stack[1] += 1
            stack[2] += 1
        elif e == x:
            partition = partition[:stack[1]] + [e] + partition[stack[1]:]
            stack[1] += 1
            stack[2] += 1
        else:
            partition = partition[:stack[2]] + [e] + partition[stack[2]:]
            stack[2] += 1
    return partition


# %%
x = 10
lst = [9, 12, 3, 5, 14, 10, 10]
partitioning(x, lst)
