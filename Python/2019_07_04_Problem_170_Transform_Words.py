#!/usr/bin/env python
# coding: utf-8
"""2019 July 4th - Daily_Coding_Problem #170."""
# <markdown>
# ## 2019 July 4th - Daily_Coding_Problem #170
#
# This problem was asked by Facebook.
#
# Given a start word, an end word, and a dictionary of valid words,
# find the shortest transformation sequence from start to end such that only
# one letter is changed at each step of the sequence,
# and each transformed word exists in the dictionary.
# If there is no possible transformation, return null.
# Each word in the dictionary have the same length as start and end
# and is lowercase.
#
# For example, given start = "dog", end = "cat",
# and dictionary = {"dot", "dop", "dat", "cat"},
# return ["dog", "dot", "dat", "cat"].
#
# Given start = "dog", end = "cat",
# and dictionary = {"dot", "tod", "dat", "dar"},
# return null as there is no possible transformation from dog to cat.


# %%
def transformWord(start, end, lst, used=[]):
    """Find the shorted way to transform the start word into the end word."""
    if used:
        start = used[-1]
    else:
        used.append(start)
    if start == end:
        return used
    ways = []
    for word in lst:
        if word not in used:
            differences = 0
            for i in range(len(word)):
                if word[i] != start[i]:
                    differences += 1
            if differences == 1:
                way = transformWord(start, end, lst, used + [word])
                if way:
                    ways.append(way)
    if not ways:
        return None
    minLength = min([len(w) for w in ways])
    return [w for w in ways if len(w) == minLength][0]


# %%
transformWord('dog', 'cat', ['dot', 'dop', 'dat', 'cat'])
