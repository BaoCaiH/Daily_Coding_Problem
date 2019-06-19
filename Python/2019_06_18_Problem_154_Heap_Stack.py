#!/usr/bin/env python
# coding: utf-8
"""2019 June 18th - Daily_Coding_Problem #154."""
# <markdown>
# ## 2019 June 18th - Daily_Coding_Problem #154
#
# This problem was asked by Amazon.
#
# Implement a stack API using only a heap.
# A stack implements the following methods:
#
# `push(item)`, which adds an element to the stack
# `pop()`, which removes and returns the most recently added element
# (or throws an error if there is nothing on the stack)
#
# Recall that a heap has the following operations:
#
# `push(item), which adds a new key to the heap
# pop(), which removes and returns the max value of the heap`


# %%
class HeapStack:
    """A Stack class which uses only heap."""

    def __init__(self):
        """Initialize the stack."""
        import sys
        self.id = sys.maxsize
        self.stack = []

    def push(self, value):
        """Push the new value into the stack."""
        from heapq import heappush
        heappush(self.stack, (self.id, value))
        self.id -= 1

    def pop(self):
        """Pop and return the latest value."""
        from heapq import heappop
        if not self.stack:
            return None
        _, value = heappop(self.stack)
        return value


# %%
stack = HeapStack()
for e in [2, 6, 8, 3, 8, 0, 3, 8, 9, 2, 4, 7, 2]:
    stack.push(e)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
