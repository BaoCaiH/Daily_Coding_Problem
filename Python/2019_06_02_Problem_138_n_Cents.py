#!/usr/bin/env python
# coding: utf-8
"""2019 June 2nd - Daily_Coding_Problem #138."""
# <markdown>
# ## 2019 June 2nd - Daily_Coding_Problem #138
#
# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a
# 10¢, a 5¢, and a 1¢.


# %%
def nCents(n):
    """Return the number of coins to make n cents."""
    options = [25, 10, 5, 1]
    value = 0
    nCoins = 0
    for coin in options:
        while value + coin <= n:
            value += coin
            nCoins += 1
    return nCoins


# %%
nCents(135)
