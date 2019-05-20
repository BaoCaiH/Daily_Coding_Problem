#!/usr/bin/env python
# coding: utf-8
"""2019 May 17th - Daily_Coding_Problem #122."""
# <markdown>
# ## 2019 May 17th - Daily_Coding_Problem #122
#
# Problem: You are given a 2-d matrix where each cell represents
# number of coins in that cell. Assuming we start at matrix[0][0],
# and can only move right or down,
# find the maximum number of coins you can collect by the bottom right corner.
#
# For example, in this matrix
#
# `0 3 1 1
# 2 0 0 4
# 1 5 3 1`
#
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


# %%
def collectMaxCoins(matrix, position=(0, 0)):
    """Move through the matrix and collect maximum number of coins."""
    r = position[0]
    c = position[1]
    nrow = len(matrix) - 1
    ncol = len(matrix[0]) - 1
    if nrow == r and ncol == c:
        return matrix[r][c]
    down = -1
    right = -1
    if nrow > r:
        down = collectMaxCoins(matrix, (r+1, c))
    if ncol > c:
        right = collectMaxCoins(matrix, (r, c+1))
    return max([down, right]) + matrix[r][c]


# %%
m = [[0, 3, 1, 1],
     [2, 0, 0, 4],
     [1, 5, 3, 1]]
# %%
collectMaxCoins(m)
