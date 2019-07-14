#!/usr/bin/env python
# coding: utf-8
"""2019 July 10th - Daily_Coding_Problem #176."""
# <markdown>
# ## 2019 July 10th - Daily_Coding_Problem #176
#
# This problem was asked by Bloomberg.
#
# Determine whether there exists a one-to-one character mapping
# from one string `s1` to another `s2`.
#
# For example, given `s1 = abc` and `s2 = bcd`,
# return `true` since we can map `a` to `b`,
# `b` to `c`, and `c` to `d`.
#
# Given `s1 = foo` and `s2 = bar`, return `false` since
# the `o` cannot map to two characters.


# %%
def characterMapping(s1, s2):
    """Determine whether 2 strings can be mapped to each other."""
    if len(s1) != len(s2):
        return False
    map = {}
    for i in range(len(s1)):
        if s1[i] not in map:
            map[s1[i]] = s2[i]
        else:
            if map[s1[i]] != s2[i]:
                return False
    s2Char = list(map.values())
    distinctChar = []
    for c in s2Char:
        if c not in distinctChar:
            distinctChar.append(c)
    if len(distinctChar) != len(s2Char):
        return False
    return True


# %%
characterMapping('abb', 'def')
