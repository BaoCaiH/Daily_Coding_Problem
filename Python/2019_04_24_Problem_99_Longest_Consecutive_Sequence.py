#!/usr/bin/env python
# coding: utf-8
"""2019 April 24th - Daily_Coding_Problem #99."""
# <markdown>
# ## 2019 April 24th - Daily_Coding_Problem #99
#
# Problem: Given an unsorted array of integers,
# find the length of the longest consecutive elements sequence.
#
# For example, given [100, 4, 200, 1, 3, 2],
# the longest consecutive element sequence is [1, 2, 3, 4].
# Return its length: 4.
#
# Your algorithm should run in O(n) complexity.


# <codecell>
def longestConsecutiveSequence(arr):
    """Return the longest consecutive sequence."""
    lst = arr.copy()
    import heapq
    heapq.heapify(lst)
    max_ = 0
    counter = 0
    prev = None
    curr = None
    for _ in range(len(lst)):
        prev = curr
        curr = heapq.heappop(lst)
        if not prev:
            counter += 1
        else:
            if curr - 1 == prev:
                counter += 1
            else:
                max_ = max(max_, counter)
                counter = 0
    return max_


# %%
a = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveSequence(a))
