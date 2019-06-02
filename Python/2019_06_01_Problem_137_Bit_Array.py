#!/usr/bin/env python
# coding: utf-8
"""2019 June 1st - Daily_Coding_Problem #137."""
# <markdown>
# ## 2019 June 1st - Daily_Coding_Problem #137
#
# Problem: Implement a bit array.
#
# A bit array is a space efficient array that holds
# a value of 1 or 0 at each index.
#
# `init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.`


# %%
class BitArray:
    """A bit array class."""

    def __init__(self, size):
        """Initialize a bit array."""
        self.size = size
        self.inds = []

    def set(self, i, val):
        """Set a value at index i."""
        if i >= self.size:
            print('Index out of list')
        if val == 0:
            if i in self.inds:
                self.inds.pop(self.inds.index(i))
        else:
            if i not in self.inds:
                self.inds.append(i)

    def get(self, i):
        """Get the value at index i."""
        if i >= self.size:
            print('Index out of list')
            return None
        return int(i in self.inds)


# %%
bit = BitArray(10)
bit.set(8, 1)
bit.get(10)
