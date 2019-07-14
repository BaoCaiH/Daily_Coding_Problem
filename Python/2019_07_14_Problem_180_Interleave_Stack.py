#!/usr/bin/env python
# coding: utf-8
"""2019 July 14th - Daily_Coding_Problem #180."""
# <markdown>
# ## 2019 July 14th - Daily_Coding_Problem #180
#
# This problem was asked by Google.
#
# Given a stack of N elements, interleave the first half of the stack with
# the second half reversed using only one other queue.
# This should be done in-place.
#
# Recall that you can only push or pop from a stack,
# and enqueue or dequeue from a queue.
#
# For example, if the stack is [1, 2, 3, 4, 5],
# it should become [1, 5, 2, 4, 3].
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
#
# Hint: Try working backwards from the end state.


# %%
def interleaveStack(stack):
    """Interleave the first half and the second half of the stack."""
    odd = len(stack) % 2
    queue = [stack.pop(0)]
    half = len(stack) // 2
    for _ in range(half):
        queue.append(stack.pop())
        queue.append(stack.pop(0))
    if odd != 1:
        queue.append(stack.pop())
    return queue


# %%
interleaveStack([1, 2, 3, 4, 5])
