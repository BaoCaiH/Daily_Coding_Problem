#!/usr/bin/env python
# coding: utf-8
"""2019 June 25th - Daily_Coding_Problem #161."""
# <markdown>
# ## 2019 June 25th - Daily_Coding_Problem #161
#
# This problem was asked by Facebook.
#
# Given a 32-bit integer, return the number with its bits reversed.
#
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.
#
# Note: The example given by the question is extremely terrible and misleading
#
# Why the hell is the example semi-symetrical, what good does it do?
#
# Another example is that given the number 13 ~ 1101,
# the result should be 11 ~ 1011


# %%
def reverseBits(n):
    """Reverse the number, bit-wise."""
    print('The initial bits are {}'.format(bin(n)))
    reverse = 0
    while n > 0:
        reverse <<= 1
        reverse |= (n & 1)
        n >>= 1
    print('The result bits are {}'.format(bin(reverse)))
    return reverse


# %%
reverseBits(13)
