#!/usr/bin/env python
# coding: utf-8
"""Merge sort functino."""
# <markdown>
# For future use of course


def mergeSort(seg):
    """Implement merge sort."""
    if len(seg) == 2:
        if seg[0] > seg[1]:
            return [seg[1], seg[0]]
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
