#!/usr/bin/env python
# coding: utf-8
"""2019 May 29th - Daily_Coding_Problem #134."""
# <markdown>
# ## 2019 May 29th - Daily_Coding_Problem #134
#
# Problem: You have a large array with most of the elements as zero.
#
# Use a more space-efficient data structure, SparseArray,
# that implements the same interface:
#
# `init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.`


# %%
class SparseArray:
    """A more space efficient data structure."""

    def __init__(self):
        """Store the values in dictionary."""
        self.values = {}

    def init(self, arr, size):
        """Copy the values from the original array."""
        self.size = size
        for i, val in enumerate(arr):
            if val:
                self.values[i] = val

    def set(self, i, val):
        """Update a value at index i."""
        if not val:
            del self.values[i]
        else:
            self.values[i] = val

    def get(self, i):
        """Return the value at index i."""
        try:
            return self.values[i]
        except KeyError:
            if i > self.size - 1:
                print('List out of index')
                return None
            return 0


# %%
sArray = SparseArray()
sArray.init([1, 0, 0, 0, 2, 0, 5, 6], 8)
sArray.get(8)
