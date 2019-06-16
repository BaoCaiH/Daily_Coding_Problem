#!/usr/bin/env python
# coding: utf-8
"""2019 June 6th - Daily_Coding_Problem #142."""
# <markdown>
# ## 2019 June 6th - Daily_Coding_Problem #142
#
# This problem was asked by Google.
#
# You're given a string consisting solely of (, ), and *.
# * can represent either a (, ), or an empty string.
# Determine whether the parentheses are balanced.
#
# For example, (()* and (*) are balanced. )*( is not balanced.


# %%
def isBalance(string):
    """Check if the string is balanced."""
    halfLength = len(string)//2
    if len(string) % 2 == 1:
        if string[halfLength] != '*':
            return False
        for i in range(halfLength):
            if string[halfLength-i-1] == ')' and string[halfLength+i+1] == '(':
                return False
    else:
        for i in range(halfLength):
            if string[halfLength-i-1] == ')' and string[halfLength+i] == '(':
                return False
    return True


# %%
a = '(()*'
b = '(*)'
c = ')*('
isBalance(c)
