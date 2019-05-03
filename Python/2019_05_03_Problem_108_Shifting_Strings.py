#!/usr/bin/env python
# coding: utf-8
"""2019 May 3rd - Daily_Coding_Problem #108."""
# <markdown>
# ## 2019 May 3rd - Daily_Coding_Problem #108
#
# Problem: Given two strings A and B,
# return whether or not A can be shifted some number of times to get B.
#
# For example, if A is abcde and B is cdeab, return true.
# If A is abc and B is acb, return false.


# %%
def transformable(a, b):
    """Check if the two strings are the same after shifting."""
    if len(a) != len(b):
        return False
    length = len(a)
    for i in range(-1, -length-1, -1):
        if b[i] == a[0]:
            if a == ''.join([b[i+j] for j in range(length)]):
                return True
    return False


# %%
a = 'abecde'
b = 'cdeabe'
transformable(a, b)
