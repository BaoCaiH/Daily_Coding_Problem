#!/usr/bin/env python
# coding: utf-8
"""2019 May 8th - Daily_Coding_Problem #113."""
# <markdown>
# ## 2019 May 8th - Daily_Coding_Problem #113
#
# Problem: Given a string of words delimited by spaces,
# reverse the words in string. For example, given "hello world here",
# return "here world hello"
#
# Follow-up: given a mutable string representation,
# can you perform this operation in-place?


# %%
def reverseString(string):
    """Reverse the given string."""
    return ' '.join(reversed(string.split()))


# %%
reverseString('hi hello what are you looking at?')
