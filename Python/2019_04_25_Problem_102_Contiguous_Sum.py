#!/usr/bin/env python
# coding: utf-8
"""2019 April 27th - Daily_Coding_Problem #102."""
# <markdown>
# ## 2019 April 27th - Daily_Coding_Problem #102
#
# Problem: Given a list of integers and a number K,
# return which contiguous elements of the list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9,
# then it should return [2, 3, 4], since 2 + 3 + 4 = 9.


# <codecell>
def contiguousSum(lst, k, contiguousLst=[]):
    """Return the contiguous number sum to K."""
    if not lst:
        if sum(contiguousLst) == k:
            return contiguousLst
        else:
            return None
    elif lst[0] == k:
        return [lst[0]]
    elif lst[0] > k:
        if sum(contiguousLst) == k:
            return contiguousLst
        else:
            return None
    else:
        contiguousLst = contiguousLst + [lst[0]]
        if sum(contiguousLst) == k:
            return contiguousLst
        elif sum(contiguousLst) > k:
            return contiguousSum(lst[1:], k, [lst[0]])
        else:
            continuous = contiguousSum(lst[1:], k, contiguousLst)
            fromHere = contiguousSum(lst[1:], k, [lst[0]])
            return [continuous, fromHere][continuous is None]


# %%
contiguousSum([1, 2, 3, 4, 5], 10)
