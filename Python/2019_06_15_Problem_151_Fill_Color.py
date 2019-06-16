#!/usr/bin/env python
# coding: utf-8
"""2019 June 15th - Daily_Coding_Problem #151."""
# <markdown>
# ## 2019 June 15th - Daily_Coding_Problem #151
#
# Given a 2-D matrix representing an image,
# a location of a pixel in the screen and a color C,
# replace the color of the given pixel and
# all adjacent same colored pixels with C.
#
# For example, given the following matrix, and location pixel of (2, 2),
# and 'G' for green:
#
# `B B W
# W W W
# W W W
# B B B`
#
# Becomes
#
# `B B G
# G G G
# G G G
# B B B`


# %%
def neighbours(current, sizes):
    """
    Return the neighbouring cells.

    Current is the current position of a cell, given by the format (row, col)

    Sizes is the sizes of the 2D matrix, given by the format (nRow, nCol)
    """
    neighbour = []
    h, w = sizes
    r, c = current
    if r > 0:
        neighbour.append((r - 1, c))
    if r < h - 1:
        neighbour.append((r + 1, c))
    if c > 0:
        neighbour.append((r, c - 1))
    if c < w - 1:
        neighbour.append((r, c + 1))
    return neighbour


def fillColor(matrix, location, color):
    """Fill all adjacent cells with one same color."""
    referenceColor = matrix[location[0]][location[1]]
    h = len(matrix)
    w = len(matrix[0])
    changeCells = []
    tempCells = []
    neighbourCells = neighbours(location, (h, w))
    for r, c in neighbourCells:
        if matrix[r][c] == referenceColor:
            tempCells.append((r, c))
    counter = 0
    while tempCells and counter < 10:
        counter += 1
        changeCells = changeCells + tempCells
        neighbourCells = []
        for cell in tempCells:
            neighbourCells = neighbourCells + neighbours(cell, (h, w))
        tempCells = []
        for r, c in neighbourCells:
            if (r, c) not in changeCells and matrix[r][c] == referenceColor:
                tempCells.append((r, c))
    for r, c in changeCells:
        matrix[r][c] = color


# %%
mtx = [['B', 'B', 'W'],
       ['W', 'W', 'W'],
       ['W', 'W', 'W'],
       ['B', 'B', 'B']]
for l in mtx:
    print(l)
# %%
fillColor(mtx, (0, 0), 'R')
fillColor(mtx, (2, 2), 'G')
# %%
for l in mtx:
    print(l)
