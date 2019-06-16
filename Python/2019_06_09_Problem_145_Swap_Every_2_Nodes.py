#!/usr/bin/env python
# coding: utf-8
"""2019 June 9th - Daily_Coding_Problem #145."""
# <markdown>
# ## 2019 June 9th - Daily_Coding_Problem #145
#
# This problem was asked by Google.
#
# Given the head of a singly linked list,
# swap every two nodes and return its head.
#
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


# %%
class Node:
    """Node class for the linked list."""

    def __init__(self, value):
        """Initialize the node."""
        self.value = value
        self.next = None


def swapPairs(node):
    """Swap every 2 nodes and return the new head."""
    prev = node
    counter = 0
    while node:
        node = node.next
        counter += 1
        if not node:
            break
        if counter == 1:
            head = node
        if counter % 2 == 1:
            prev.next = node.next
            node.next = prev
            node = prev
        else:
            if node.next:
                prev.next = node.next
            prev = node
    return head


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
result = swapPairs(a)
# %%
result.next.next.next.next.value
