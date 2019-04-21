#!/usr/bin/env python
# coding: utf-8
"""2019 April 21th - Daily_Coding_Problem #96."""
# <markdown>
# ## 2019 April 21th - Daily_Coding_Problem #96
#
# Problem: Given a number in the form of a list of digits,
# return all possible permutations.
#
# For example, given [1,2,3],
# return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


# <codecell>
def allPermutation(lst):
    """Return the all the possible permutations."""
    # Return an empty list in list if the last element is used
    if not lst:
        return [[]]

    # For each number at any one position, recurse the rest of the numbers
    # and concat the returned combinations to the given element
    permutations = []
    for i, e in enumerate(lst):
        permutations = permutations +\
            [[e] + com for com in allPermutation(lst[:i]+lst[i+1:])]
    return permutations


# %%
# [1, 2, 3, 4]
# [1, 2, 4, 3]
# [1, 3, 2, 4]
# [1, 3, 4, 2]
# [1, 4, 2, 3]x
# [1, 4, 3, 2]
# [2, 1, 3, 4]
l1 = [1, 3, 2, 4]
print(l1)

# %%
print(allPermutation(l1))
