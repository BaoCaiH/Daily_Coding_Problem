#!/usr/bin/env python
# coding: utf-8
"""2019 May 13th - Daily_Coding_Problem #118."""
# <markdown>
# ## 2019 May 13th - Daily_Coding_Problem #118
#
# Problem: Given a sorted list of integers, square the elements
# and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


# %%
def squareAndSort(lst):
    """Square all elements and sort them."""
    lst = [e**2 for e in lst]
    lst.sort()
    return lst


# %%
a = [-9, -2, 0, 2, 3, -10]
print(a)
b = squareAndSort(a)

# %%
print(b)
