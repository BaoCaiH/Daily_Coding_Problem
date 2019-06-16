#!/usr/bin/env python
# coding: utf-8
"""2019 June 12th - Daily_Coding_Problem #148."""
# <markdown>
# ## 2019 June 12th - Daily_Coding_Problem #148
#
# This problem was asked by Apple.
#
# Gray code is a binary code where each successive value
# differ in only one bit, as well as when wrapping around.
# Gray code is common in hardware so that we don't see temporary
# spurious values during transitions.
#
# Given a number of bits n, generate a possible gray code for it.
#
# For example, for n = 2, one gray code would be [00, 01, 11, 10].


# %%
def generateGrayCode(n):
    """Generate a gray code."""
    if n == 0:
        return ['']
    else:
        grayCode = generateGrayCode(n-1)
        zero = ['0' + gc for gc in grayCode]
        one = ['1' + gc for gc in reversed(grayCode)]
        return zero + one


# %%
generateGrayCode(4)
