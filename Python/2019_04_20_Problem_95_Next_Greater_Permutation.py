#!/usr/bin/env python
# coding: utf-8
"""2019 April 20th - Daily_Coding_Problem #95."""
# <markdown>
# ## 2019 April 20th - Daily_Coding_Problem #95

# Problem: Given a number represented by a list of digits,
# find the next greater permutation of a number, in terms of
# lexicographic ordering. If there is not greater permutation possible,
# return the permutation with the lowest value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2]
# should return [2,1,3]. The list [3,2,1] should return [1,2,3].

# Can you perform the operation without allocating extra memory
# (disregarding the input memory)?


# <codecell>
def nextGreaterPermutation(lst):
    """
    Return the next permutation which is a larger number.

    If that is not possible, return the smallest permutation.
    """
    # If there is only 1 digit, return as it is
    if len(lst) == 1:
        return lst

    # Search list in reverse, find the index,
    # where the number is less than the one before it
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > lst[i-1]:
            break

    # If the list is in descending order, return a reversed list
    if i == 0:
        lst.reverse()
        return lst

    # If not, swap the number found above with the smallest number that is
    # larger than the number found above
    lst[lst.index(min(filter(lambda x: x > lst[i-1], lst[i:])))], lst[i-1] =\
        lst[i-1], lst[lst.index(min(filter(lambda x: x > lst[i-1], lst[i:])))]
    # Then reverse the rest of the list from the index
    lst[i:] = lst[i:][::-1]
    return lst


# %%
l1 = [1, 2, 3, 4]
print('Given the list {}'.format(l1))
# %%
print(nextGreaterPermutation(l1))
while l1 != [1, 2, 3, 4]:
    print(nextGreaterPermutation(l1))
