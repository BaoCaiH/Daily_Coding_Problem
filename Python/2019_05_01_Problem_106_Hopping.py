#!/usr/bin/env python
# coding: utf-8
"""2019 May 1st - Daily_Coding_Problem #106."""
# <markdown>
# ## 2019 May 1st - Daily_Coding_Problem #106
#
# Problem: Given an integer list where each number represents the number
# of hops you can make, determine whether you can reach to the last index
# starting at index 0.
#
# For example, `[2, 0, 1, 0]` returns true while `[1, 1, 0, 1]` returns false.


# %%
def hopping(lst):
    """Hop to the end of the list."""
    lastIndex = len(lst) - 1
    i = 0
    while i < lastIndex:
        hopDist = lst[i]
        if hopDist == 0:
            return False
        i += hopDist
    if i == lastIndex:
        return True
    return False


# %%
lst1 = [2, 0, 1, 0]
hopping(lst1)

# %%
lst2 = [1, 1, 0, 1]
hopping(lst2)

# %%
lst3 = [1, 3, 4, 7, 1, 2, 0]
hopping(lst3)
