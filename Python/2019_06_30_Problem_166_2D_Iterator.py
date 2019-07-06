#!/usr/bin/env python
# coding: utf-8
"""2019 June 30th - Daily_Coding_Problem #166."""
# <markdown>
# ## 2019 June 30th - Daily_Coding_Problem #166
#
# Implement a 2D iterator class.
# It will be initialized with an array of arrays,
# and should implement the following methods:
#
# next(): returns the next element in the array of arrays.
# If there are no more elements, raise an exception.
#
# has_next(): returns whether or not the iterator still has elements left.
#
# For example, given the input [[1, 2], [3], [], [4, 5, 6]],
# calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
#
# Do not use flatten or otherwise clone the arrays.
# Some of the arrays can be empty.


# %%
class Iterator2D:
    """A 2D iterator class."""

    def __init__(self, array):
        """Initialize with a 2d array."""
        self.array = array
        self.next_ = None
        if len(self.array) != 0:
            for i, a in enumerate(self.array):
                if len(a) != 0:
                    self.next_ = self.array[i][0]
                    self.currCounter = 1
                    self.arrayCounter = i
                    break

    def next(self):
        """Return the next element."""
        if not self.next_:
            raise Exception('The array has no next value.')
            return self.next
        next = self.next_
        if len(self.array[self.arrayCounter]) > self.currCounter:
            self.next_ = self.array[self.arrayCounter][self.currCounter]
            self.currCounter += 1
        else:
            if len(self.array) <= self.arrayCounter+1:
                self.next_ = None
            else:
                for i, a in enumerate(self.array[self.arrayCounter+1:]):
                    if len(a) != 0:
                        self.next_ = self.array[self.arrayCounter+i+1][0]
                        self.currCounter = 1
                        self.arrayCounter += i+1
                        break
        return next

    def hasNext(self):
        """Check whether it has a next value."""
        return self.next_ is not None


# %%
arr = [[1, 2], [3], [], [4, 5, 6]]
# %%
iter2D = Iterator2D(arr)
for _ in range(6):
    print(iter2D.next())
# %%
arr
