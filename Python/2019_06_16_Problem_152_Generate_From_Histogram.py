#!/usr/bin/env python
# coding: utf-8
"""2019 June 16th - Daily_Coding_Problem #152."""
# <markdown>
# ## 2019 June 16th - Daily_Coding_Problem #152
#
# This problem was asked by Triplebyte.
#
# You are given n numbers as well as n probabilities that sum up to 1.
# Write a function to generate one of the numbers with its corresponding
# probability.
#
# For example, given the numbers [1, 2, 3, 4] and probabilities
# [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time,
# 2 50% of the time, and 3 and 4 20% of the time.
#
# You can generate random numbers between 0 and 1 uniformly.


# %%
def generateFromHistogram(values, probs):
    """Return a value with its corresponding probability."""
    from random import random
    prob = random()
    cummulative = 0
    for i, e in enumerate(probs):
        if prob <= cummulative + e and prob > cummulative:
            return values[i]
        cummulative += e


# %%
generateFromHistogram([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
