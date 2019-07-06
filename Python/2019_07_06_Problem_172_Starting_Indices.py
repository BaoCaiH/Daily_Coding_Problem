#!/usr/bin/env python
# coding: utf-8
"""2019 July 6th - Daily_Coding_Problem #172."""
# <markdown>
# ## 2019 July 6th - Daily_Coding_Problem #172
#
# This problem was asked by Dropbox.
#
# Given a string s and a list of words words,
# where each word is the same length,
# find all starting indices of substrings in s that is a
# concatenation of every word in words exactly once.
#
# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
# return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at
# index 13.
#
# Given s = "barfoobazbitbyte" and words = ["dog", "cat"],
# return [] since there are no substrings composed of "dog" and "cat" in s.
#
# The order of the indices does not matter.


# %%
def allPermutation(words):
    """Return all the permutation of the word list."""
    if len(words) == 1:
        return words
    lst = []
    for i, word in enumerate(words):
        lst = lst + [word + w for w in allPermutation(words[:i]+words[i+1:])]
    return lst


def startingIndices(s, words):
    """Find all the starting indices which contains one of the permutation."""
    permutations = allPermutation(words)
    permutationLength = len(permutations[0])
    sLength = len(s)
    indices = []
    for i in range(sLength):
        if (sLength - i - permutationLength) >= 0:
            if s[i:i+permutationLength] in permutations:
                indices.append(i)
    return indices


# %%
s = "dogcatcatcodecatdog"
words = ['cat', 'dog']
startingIndices(s, words)
