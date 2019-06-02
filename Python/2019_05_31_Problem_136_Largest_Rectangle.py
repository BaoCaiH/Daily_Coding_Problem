#!/usr/bin/env python
# coding: utf-8
"""2019 May 31st - Daily_Coding_Problem #136."""
# <markdown>
# ## 2019 May 31st - Daily_Coding_Problem #136
#
# Problem: Given an N by M matrix consisting only of 1's and 0's,
# find the largest rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# `[[1, 0, 0, 0],
#   [1, 0, 1, 1],
#   [1, 0, 1, 1],
#   [0, 1, 0, 0]]`
#
# Return 4.


# %%
def isValidRectangle(mtx, r, c, i, j):
    """Find if the rectangle is valid."""
    for row in range(r, r+i+1):
        for col in range(c, c+j+1):
            if mtx[row][col] == 0:
                return False
    return True


def largestRectangle(mtx):
    """Find the largest triangle in the 2D matrix."""
    nRow = len(mtx)
    nCol = len(mtx[0])
    largestArea = 0
    for r in range(nRow):
        for c in range(nCol):
            maxR = nRow - r
            maxC = nCol - c
            for i in range(maxR):
                for j in range(maxC):
                    if isValidRectangle(mtx, r, c, i, j):
                        if (i+1)*(j+1) > largestArea:
                            largestArea = (i+1)*(j+1)
    return largestArea


# %%
matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 1, 1]]
largestRectangle(matrix)
