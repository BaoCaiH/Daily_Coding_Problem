#!/usr/bin/env python
# coding: utf-8
"""2019 June 11th - Daily_Coding_Problem #147."""
# <markdown>
# ## 2019 June 11th - Daily_Coding_Problem #147
#
# Given a list, sort it using this method: reverse(lst, i, j),
# which reverses lst from i to j.


# %%
def reverse(lst, i, j):
    """Reverse a portion of a list."""
    return lst[:i] + list(reversed(lst[i:j+1])) + lst[j+1:]


def mergeSort(seg):
    """Implement merge sort."""
    if len(seg) == 2:
        if seg[0] > seg[1]:
            return reverse(seg, 0, 1)
        else:
            return seg
    elif len(seg) == 1:
        return seg
    else:
        sortedSeg1 = mergeSort(seg[:(len(seg)//2)])
        sortedSeg2 = mergeSort(seg[(len(seg)//2):])
        merged = []
        length1 = len(sortedSeg1)
        length2 = len(sortedSeg2)
        i, j = 0, 0
        while i < length1 and j < length2:
            if sortedSeg1[i] <= sortedSeg2[j]:
                merged.append(sortedSeg1[i])
                i += 1
            else:
                merged.append(sortedSeg2[j])
                j += 1
        merged = merged + [sortedSeg1[i:], sortedSeg2[j:]][i == length1]
        return merged


# %%
lst = [0, 6, 4, 2, 5, 3, 1]
print(lst)
mergeSort(lst)
