#!/usr/bin/env python
# coding: utf-8
"""2019 July 3rd - Daily_Coding_Problem #169."""
# <markdown>
# ## 2019 July 3rd - Daily_Coding_Problem #169
#
# This problem was asked by Google.
#
# Given a linked list, sort it in O(n log n) time and constant space.
#
# For example, the linked list 4 -> 1 -> -3 -> 99
# should become -3 -> 1 -> 4 -> 99.


# %%
class Node:
    """A node of the linked list."""

    def __init__(self, value):
        """Initialize the node."""
        self.value = value
        self.next = None


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


def sortList(head):
    """Sort the linked list."""
    nodeDict = {}
    valueLst = []
    while head:
        if head.value not in nodeDict:
            nodeDict[head.value] = []
        valueLst.append(head.value)
        nodeDict[head.value].append(head)
        head = head.next
    sortedValue = mergeSort(valueLst)
    prev = None
    for i, v in enumerate(sortedValue):
        if i == 0:
            newHead = nodeDict[v].pop()
            prev = newHead
        elif i == len(sortedValue)-1:
            prev.next = nodeDict[v].pop()
            prev.next.next = None
        else:
            prev.next = nodeDict[v].pop()
            prev = prev.next
    return newHead


# %%
a = Node(4)
b = Node(1)
c = Node(-3)
d = Node(99)
a.next = b
b.next = c
c.next = d
# %%
n = sortList(a)
# %%
n.value
