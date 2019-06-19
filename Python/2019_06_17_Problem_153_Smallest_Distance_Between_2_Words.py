#!/usr/bin/env python
# coding: utf-8
"""2019 June 17th - Daily_Coding_Problem #153."""
# <markdown>
# ## 2019 June 17th - Daily_Coding_Problem #153
#
# Find an efficient algorithm to find the smallest distance
# (measured in number of words) between any two given words in a string.
#
# For example, given words "hello", and "world" and a text content
# of "dog cat hello cat dog dog hello cat world",
# return 1 because there's only one word "cat" in between the two words.


# %%
def fromWordToWord(string, word1, word2):
    """Find the sortest distance between 2 words."""
    smallestDistance = None
    refWord, refIndex = None, None
    for i, word in enumerate(string.split()):
        print(word)
        if word == word1 or word == word2:
            if not refWord:
                refWord = word
                refIndex = i
            else:
                if word != refWord:
                    if not smallestDistance:
                        smallestDistance = i-refIndex-1
                    else:
                        smallestDistance = min(smallestDistance, i-refIndex-1)
                refWord = word
                refIndex = i
    return smallestDistance


# %%
stg = "world dog cat hello cat dog dog hello cat world"
# %%
fromWordToWord(stg, 'hello', 'world')
