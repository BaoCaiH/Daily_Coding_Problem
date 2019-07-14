#!/usr/bin/env python
# coding: utf-8
"""2019 July 11th - Daily_Coding_Problem #177."""
# <markdown>
# ## 2019 July 11th - Daily_Coding_Problem #177
#
# This problem was asked by Airbnb.
#
# Given a linked list and a positive integer k,
# rotate the list to the right by k places.
#
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2,
# it should become 3 -> 5 -> 7 -> 7.
#
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3,
# it should become 3 -> 4 -> 5 -> 1 -> 2.


# %%
class Node:
    """Nodes to store values."""

    def __init__(self, value, next=None):
        """Initialize the node."""
        self.value = value
        self.next = next


def rotateLinkedList(head, k):
    """Rotate the linked list to the right by k steps."""
    nodeList = []
    while head:
        nodeList.append(head)
        head = head.next
    nodeList[-1].next = nodeList[0]
    position = k % len(nodeList)
    nodeList[position-1].next = None
    return nodeList[position]


# %%
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
# %%
result = rotateLinkedList(a, 2)

# %%
result.next.next.next.next.value
