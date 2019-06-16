#!/usr/bin/env python
# coding: utf-8
"""2019 June 7th - Daily_Coding_Problem #143."""
# <markdown>
# ## 2019 June 7th - Daily_Coding_Problem #143
#
# This problem was asked by Google.
#
# Given an array of numbers and an index i,
# return the index of the nearest larger number of the number at index i,
# where distance is measured in array indices.
#
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
#
# If two distances to larger numbers are the equal,
# then return any one of them.
# If the array at i doesn't have a nearest larger integer, then return null.
#
# Follow-up: If you can preprocess the array, can you do this in constant time?


# %%
def preprocessing(lst):
    """Preprocess the number array."""
    processed = {}
    for i, e in enumerate(lst):
        minDist = len(lst)
        for j, f in enumerate(lst):
            if f > e:
                minDist = min(minDist, abs(i-j))
        if minDist == len(lst):
            processed[i] = 'The largest element'
        else:
            processed[i] = minDist
    return processed


def nearestLarger(index, lst):
    """Return the distance to the nearest larger number."""
    if index >= len(lst):
        print('Index out of list')
        return None

    processed = preprocessing(lst)

    return processed[index]


# %%
lst = [4, 1, 3, 5, 6]
nearestLarger(4, lst)
