#!/usr/bin/env python
# coding: utf-8
"""2019 May 4th - Daily_Coding_Problem #109."""
# <markdown>
# ## 2019 May 4th - Daily_Coding_Problem #109
#
# Problem: Given an unsigned 8-bit integer, swap its even and odd bits.
# The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped,
# and so on.
#
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
#
# Bonus: Can you do this in one line?


# %%
def swapBits(num):
    """Swap every bits pair, odds with evens, left with right."""
    # 85 is 01010101 in 8bits binary,
    # Compare (&) it with the number will return the activated right bits
    # 170 is 85 counterpart in 8bits, so activated left bits
    # Then the shift (<<) the right to left, (>>)left to right by 1 position
    # Take all the activated bits from either side (|)
    # Only work for 8bits, higher bits need different reference numbers
    # Edit: it does now, only with unsigned integer though

    # Preparation, find the required number of bits
    halfBase = 1+len((bin(num)[2:]))//2
    right = int('01'*halfBase, 2)
    left = int('10'*halfBase, 2)
    # The actual operation takes only 1 line
    return ((num & right) << 1) | ((num & left) >> 1)


# %%
n = int(input('Given an integer number:'))
print(bin(n))
print(bin(swapBits(n)))
