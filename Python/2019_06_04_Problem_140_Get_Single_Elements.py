#!/usr/bin/env python
# coding: utf-8
"""2019 June 4th - Daily_Coding_Problem #140."""
# <markdown>
# ## 2019 June 4th - Daily_Coding_Problem #140
#
# This problem was asked by Facebook.
#
# Given an array of integers in which two elements appear exactly once
# and all other elements appear exactly twice,
# find the two elements that appear only once.
#
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
# The order does not matter.
#
# Follow-up: Can you do this in linear time and constant space?
#
# The solution will run in (2N) time
# Using bit operations xor, the elements appear twice will eliminate each other
#
# Leaving only the xor results of the 2 distinct elements
#
# The xor will contain only the bits from either sides of the distinct elements
#
# Use the first available bit from the right as a reference to find out which
# of the number in the array is one of the distinct elements.
#
# Assignment will also be done by bit operator xor so the elements that
# accidentally match the reference will also be eliminated


# %%

def singleElements(array):
    """Find the single elements in the given array."""
    # Get the xor of the 2 distinct elements
    xor = array[0]
    for n in array[1:]:
        xor ^= n

    # Zero will have no bit activated
    x, y = 0, 0

    # Get the first bit from the right
    firstBit = (xor & ~(xor - 1))
    for n in array:
        if n & firstBit:
            # This will eliminate duplicates
            x ^= n
        else:
            y ^= n

    return (x, y)


# %%
a = [1, 4, 6, 11, 10, 1, 6, 10]
singleElements(a)
