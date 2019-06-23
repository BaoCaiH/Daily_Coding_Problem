#!/usr/bin/env python
# coding: utf-8
"""2019 June 22nd - Daily_Coding_Problem #158."""
# <markdown>
# ## 2019 June 22nd - Daily_Coding_Problem #158
#
# This problem was asked by Slack.
#
# You are given an N * M matrix of 0s and 1s.
# Starting from the top left corner,
# how many ways are there to reach the bottom right corner?
#
# You can only move right and down.
# 0 represents an empty space while 1 represents a wall you cannot walk through
#
# For example, given the following matrix:
#
# `[[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]`
#
# Return 2, as there are only two ways to get to the bottom right:
#
# Right, down, down, right
#
# Down, right, down, right
#
# The top left corner and bottom right corner will always be 0.


# %%
def waysThroughMatrix(matrix, start=(0, 0)):
    """Return the number of ways to move through the matrix."""
    if (start[0] == len(matrix)-1 and start[0] >= len(matrix[0])-2) or\
       (start[0] >= len(matrix)-2 and start[0] == len(matrix[0])-1):
        return 1
    counter = 0
    if matrix[start[0]+1][start[1]] == 0:
        counter += waysThroughMatrix(matrix, (start[0]+1, start[1]))
    if matrix[start[0]][start[1]+1] == 0:
        counter += waysThroughMatrix(matrix, (start[0], start[1]+1))
    return counter


# %%
matrix = [[0, 0, 1],
          [0, 0, 1],
          [1, 0, 0]]
waysThroughMatrix(matrix)
