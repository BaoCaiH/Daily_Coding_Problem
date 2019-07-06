#!/usr/bin/env python
# coding: utf-8
"""2019 July 2nd - Daily_Coding_Problem #168."""
# <markdown>
# ## 2019 July 2nd - Daily_Coding_Problem #168
#
# This problem was asked by Facebook.
#
# Given an N by N matrix, rotate it by 90 degrees clockwise.
#
# For example, given the following matrix:
#
# `[[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]`
#
# you should return:
#
# `[[7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]]`
#
# Follow-up: What if you couldn't use any extra space?


# %%
def rotateMatrix(mtx):
    """Rotate the matrix 90 degree."""
    rotated = []
    for _ in range(len(mtx[0])):
        rotated.append([mtx[i].pop(0) for i in range(len(mtx)-1, -1, -1)])
    return rotated


# %%
mtx = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]]
rotateMatrix(mtx)
