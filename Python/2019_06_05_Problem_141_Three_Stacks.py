#!/usr/bin/env python
# coding: utf-8
"""2019 June 5th - Daily_Coding_Problem #141."""
# <markdown>
# ## 2019 June 5th - Daily_Coding_Problem #141
#
# This problem was asked by Microsoft.
#
# Implement 3 stacks using a single list:
#
# `class Stack:
#     def __init__(self):
#         self.list = []
#
#     def pop(self, stack_number):
#         pass
#
#     def push(self, item, stack_number):
#         pass`


# %%
class Stack:
    """Three stacks in a gingle list."""

    def __init__(self):
        """Initialize the stacks."""
        self.list = []
        self.stacks = {0: 0,
                       1: 0,
                       2: 0}

    def push(self, value, stackNumber):
        """Add value to the stack."""
        self.list = self.list[:self.stacks[stackNumber]] + [value] +\
            self.list[self.stacks[stackNumber]:]
        self.stacks[2] += 1
        if stackNumber <= 1:
            self.stacks[1] += 1
        if stackNumber == 0:
            self.stacks[0] += 1

    def pop(self, stackNumber):
        """Delete and return the last number in the chosen stack."""
        if stackNumber == 0:
            if self.stacks[stackNumber] == 0:
                print('Stack 0 is empty')
                return None
        elif self.stacks[stackNumber] == self.stacks[(stackNumber-1)]:
            print('Stack {} is empty'.format(stackNumber))
            return None
        value = self.list[self.stacks[stackNumber]-1]
        self.list = self.list[:self.stacks[stackNumber]-1] +\
            self.list[self.stacks[stackNumber]:]
        self.stacks[2] -= 1
        if stackNumber <= 1:
            self.stacks[1] -= 1
        if stackNumber == 0:
            self.stacks[0] -= 1
        return value


# %%
a = Stack()
n = 0
for i in range(3):
    for j in range(4):
        a.push(n, i)
        n += 1
# %%
a.pop(0)
