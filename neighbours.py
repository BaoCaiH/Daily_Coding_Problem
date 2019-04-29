#!/usr/bin/env python
# coding: utf-8
"""
Function to return neighbouring cells.

Since I have used it far too many time to keep re-typing the function.
"""


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
        if c > 0:
            neighbour.append((r - 1, c - 1))
        if c < w - 1:
            neighbour.append((r - 1, c + 1))
    if r < h - 1:
        neighbour.append((r + 1, c))
        if c > 0:
            neighbour.append((r + 1, c - 1))
        if c < w - 1:
            neighbour.append((r + 1, c + 1))
    if c > 0:
        neighbour.append((r, c - 1))
    if c < w - 1:
        neighbour.append((r, c + 1))
    return neighbour
