#!/usr/bin/env python
# coding: utf-8
"""2019 June 13th - Daily_Coding_Problem #149."""
# <markdown>
# ## 2019 June 13th - Daily_Coding_Problem #149
#
# This problem was asked by Goldman Sachs.
#
# Given a list of numbers L, implement a method sum(i, j) which
# returns the sum from the sublist L[i:j] (including i, excluding j).
#
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3)
# should return sum([2, 3]), which is 5.
#
# You can assume that you can do some pre-processing.
# sum() should be optimized over the pre-processing step.


# %%
class OptimizedSum:
    """A class to optimize summing lists."""

    def __init__(self, lst):
        """Preprocess the list."""
        self.lst = lst
        self.totals = []
        self.total = 0
        for number in self.lst:
            self.total += number
            self.totals.append(self.total)

    def sum(self, i, j):
        """Sum the elements from i to j."""
        if i > len(self.lst) or j < 0 or j < i:
            return 0
        return self.totals[j-1] - self.totals[i]


# %%
lst = [1, 2, 3, 4, 5]
L = OptimizedSum(lst)
# %%
L.sum(1, 3)
