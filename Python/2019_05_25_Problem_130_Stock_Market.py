#!/usr/bin/env python
# coding: utf-8
"""2019 May 25th - Daily_Coding_Problem #130."""
# <markdown>
# ## 2019 May 25th - Daily_Coding_Problem #130
#
# Problem: Given an array of numbers representing the stock prices of a
# company in chronological order and an integer k,
# return the maximum profit you can make from k buys and sells.
# You must buy the stock before you can sell it, and you must sell the
# stock before you can buy it again.
#
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.


# %%
def calProfit(lst):
    """Return the profit."""
    profit = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            profit -= lst[i]
        else:
            profit += lst[i]
    return profit


def stockMarket(k, array, history=[]):
    """Calculate the maximum profit with k buys and sells."""
    if k == 0 or not array:
        return calProfit(history)
    decisions = []
    if not history or len(history) % 2 == 0:
        decisions.append(stockMarket(k, array[1:], history + [array[0]]))
        decisions.append(stockMarket(k, array[1:], history))
    else:
        decisions.append(stockMarket(k-1, array[1:], history + [array[0]]))
        decisions.append(stockMarket(k, array[1:], history))
    return max(decisions)


# %%
k = 2
stockLevels = [5, 2, 4, 0, 1]
stockMarket(k, stockLevels)
