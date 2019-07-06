#!/usr/bin/env python
# coding: utf-8
"""2019 June 26th - Daily_Coding_Problem #162."""
# <markdown>
# ## 2019 June 26th - Daily_Coding_Problem #162
#
# This problem was asked by Square.
#
# Given a list of words, return the shortest unique prefix of each word.
# For example, given the list:
#
# `dog
# cat
# apple
# apricot
# fish`
#
# Return the list:
#
# `d
# c
# app
# apr
# f`


# %%
def shortestPrefix(lst):
    """Return the shortest unique prefix of each words."""
    prefixes = {}
    for word in lst:
        if word[0] not in prefixes:
            prefixes[word[0]] = []
        prefixes[word[0]].append(word[1:])
    prefixLst = []
    for prefix, subs in prefixes.items():
        if len(subs) > 1:
            prefixLst = prefixLst+[prefix +
                                   subpre for subpre in shortestPrefix(subs)]
        else:
            prefixLst = prefixLst + [prefix]
    return prefixLst


# %%
wordLst = ['dog', 'cat', 'apple', 'apricot', 'fish']
shortestPrefix(wordLst)
