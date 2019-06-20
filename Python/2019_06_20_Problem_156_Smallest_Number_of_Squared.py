#!/usr/bin/env python
# coding: utf-8
"""2019 June 20th - Daily_Coding_Problem #156."""
# <markdown>
# ## 2019 June 20th - Daily_Coding_Problem #156
#
# This problem was asked by Facebook.
#
# Given a positive integer n,
# find the smallest number of squared integers which sum to n.
#
# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
#
# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.


# %%
def smallestNumberOfSquared(n):
    """Find the smallest number of squared integers which sum to n."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    integer = 1
    while integer <= n//2:
        if (integer+1)**2 > n:
            print('Integer: {}'.format(integer))
            return 1 + smallestNumberOfSquared(n-integer**2)
        integer += 1


# %%
n = 9576474857636
print('n is {}'.format(n))
smallestNumberOfSquared(n)
