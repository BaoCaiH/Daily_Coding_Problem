#!/usr/bin/env python
# coding: utf-8
"""2019 May 9th - Daily_Coding_Problem #114."""
# <markdown>
# ## 2019 May 9th - Daily_Coding_Problem #114
#
# Problem: Given a string and a set of delimiters,
# reverse the words in the string while maintaining the relative order
# of the delimiters. For example, given "hello/world:here",
# return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases:
# "hello/world:here/", "hello//world:here"


# %%
def reverseString(string, delimiterSet=' '):
    """Reverse the given string and a delimiter set."""
    length = len(string)
    words = []
    delims = []
    word = ''
    delim = ''
    for i in range(length):
        if string[i] not in delimiterSet:
            word = word + string[i]
            if delim:
                delims.append(delim)
                delim = ''
        else:
            delim = delim + string[i]
            if word:
                words.append(word)
                word = ''
    if word:
        words.append(word)
        words.reverse()
        if len(words) == len(delims):
            return ''.join([delims[i]+words[i] for i in range(len(words))])
        else:
            return ''.join([words[i]+delims[i] for i in range(len(words)-1)] +
                           [words[-1]])
    if delim:
        delims.append(delim)
        words.reverse()
        if len(words) == len(delims):
            return ''.join([words[i]+delims[i] for i in range(len(delims))])
        else:
            return ''.join([delims[i]+words[i] for i in range(len(delims)-1)] +
                           [delims[-1]])


# %%
string = '/hello/world:here/'
# string = 'hello//world:here'
# string = 'hello world here'
reverseString(string, '/:')
