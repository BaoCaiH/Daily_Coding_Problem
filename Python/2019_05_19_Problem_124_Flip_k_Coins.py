#!/usr/bin/env python
# coding: utf-8
"""2019 May 19th - Daily_Coding_Problem #124."""
# <markdown>
# ## 2019 May 19th - Daily_Coding_Problem #124
#
# Problem: You have n fair coins and you flip them all at the same time.
# Any that come up tails you set aside.
# The ones that come up heads you flip again.
# How many rounds do you expect to play before only one coin remains?
#
# Write a function that, given n,
# returns the number of rounds you'd expect to play until one coin remains.


# %%
def flipCoins(n):
    """Return the number of times to flip k coins until 1 coin remains."""
    rounds = 0
    while n > 1:
        n = n/2
        rounds += 1
    return rounds


# %%
flipCoins(111)
