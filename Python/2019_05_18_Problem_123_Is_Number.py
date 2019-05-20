#!/usr/bin/env python
# coding: utf-8
"""2019 May 18th - Daily_Coding_Problem #123."""
# <markdown>
# ## 2019 May 18th - Daily_Coding_Problem #123
#
# Problem: This problem was asked by LinkedIn.

# Given a string, return whether it represents a number.
# Here are the different kinds of numbers:
#
# "10", a positive integer
# "-10", a negative integer
# "10.1", a positive real number
# "-10.1", a negative real number
# "1e5", a number in scientific notation
# And here are examples of non-numbers:
#
# "a"
# "x 1"
# "a -2"
# "-"


# %%
def isNumber(string):
    """Check if the string represents a number."""
    prefix = '+-'
    midway = '.e'
    prev = ''
    operator = None
    for i in range(len(string)):
        if not prev:
            if string[i] in prefix:
                prev = string[i]
            else:
                try:
                    int(string[i])
                    prev = string[i]
                except ValueError:
                    # print('Non-number')
                    return False
        else:
            if string[i] in midway:
                if not operator:
                    operator = string[i]
                    midway = ''.join([c for c in midway if c != operator])
                prev = string[i]
            else:
                try:
                    int(string[i])
                    prev = string[i]
                except ValueError:
                    # print('Non-number')
                    return False
    # print('Number')
    return True


# %%
s = ['10.1', '-10.1', '10e5', 'x-1']
# %%
for e in s:
    print('String: {} is {}'.format(e, isNumber(e)))
