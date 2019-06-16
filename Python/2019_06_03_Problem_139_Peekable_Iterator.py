#!/usr/bin/env python
# coding: utf-8
"""2019 June 3rd - Daily_Coding_Problem #139."""
# <markdown>
# ## 2019 June 3rd - Daily_Coding_Problem #139
#
# This problem was asked by Google.
#
# Given an iterator with methods next() and hasNext(),
# create a wrapper iterator, PeekableInterface, which also implements peek().
# peek shows the next element that would be returned on next().
#
# Here is the interface:
#
# `class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass
#
#     def peek(self):
#         pass
#
#     def next(self):
#         pass
#
#     def hasNext(self):
#         pass`


# %%
class PeekableInterface(object):
    """Peekable Interface for a iterator."""

    def __init__(self, iterator):
        """Initialize the peeking mechanism."""
        self.iterator = iterator
        self.nextValue = next(self.iterator)
        self.hasNextValue = True

    def peek(self):
        """Peek at the next value without advancing the iterator."""
        return self.nextValue

    def next(self):
        """Advancing the iterator."""
        nextValue = self.nextValue
        try:
            self.nextValue = next(self.iterator)
        except StopIteration:
            self.nextValue = None
            self.hasNextValue = False
        return nextValue

    def hasNext(self):
        """Check if there is a next value to peek at."""
        return self.hasNextValue


# %%
a = [1, 2, 3, 4, 5, 6]
b = iter(a)
# %%
c = PeekableInterface(b)
# %%
c.hasNext()
