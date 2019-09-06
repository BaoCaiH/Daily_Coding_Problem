#!/usr/bin/env python
# coding: utf-8
"""2019 July 15th - Daily_Coding_Problem #181."""
# <markdown>
# ## 2019 July 15th - Daily_Coding_Problem #181
#
# This problem was asked by Google.
#
# Given a string, split it into as few strings as possible such that
# each string is a palindrome.
#
# For example, given the input string racecarannakayak,
# return ["racecar", "anna", "kayak"].
#
# Given the input string abc, return ["a", "b", "c"].


# %%
def is_palindrome(string):
    """Check if the string is palindrome."""
    for i in range(len(string) // 2 + len(string) % 2):
        if string[i] != string[-(i+1)]:
            return False
    return True


# %%
def longest_palindrome(string):
    """Find the longest palindrome starting from the beginning."""
    palindromes = []
    for i in range(len(string)):
        if is_palindrome(string[:i+1]):
            palindromes.append(string[:i+1])
    max_length = max([(lambda x: len(x))(s) for s in palindromes])
    return string[:max_length]


# %%
def min_split(string):
    """Split the string into as few palindromes as possible."""
    s_lst = []
    n = 0
    while len(string) > 0 and n < 5:
        s_lst.append(longest_palindrome(string))
        string = string[len(s_lst[-1]):]
        n += 1
    return s_lst


# %%
test_string = 'racecarannakayak'
# %%
min_split(test_string)
