#!/usr/bin/env python
# coding: utf-8
"""2019 April 25th - Daily_Coding_Problem #100."""
# <markdown>
# ## 2019 April 25th - Daily_Coding_Problem #100
#
# Problem: You are in an infinite 2D grid where you can move in
# any of the 8 directions:
#
# (x,y) to<br>
# (x+1, y),<br>
# (x - 1, y),<br>
# (x, y+1),<br>
# (x, y-1),<br>
# (x-1, y-1),<br>
# (x+1,y+1),<br>
# (x-1,y+1),<br>
# (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover
# the points. Give the minimum number of steps in which you can achieve it.
# You start from the first point.
#
# Example: Input: [(0, 0), (1, 1), (1, 2)] Output: 2 It takes 1 step to move
# from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


# <codecell>
def neighbours(current):
    """
    Return the neighbouring cells.

    Current is the current position of a cell, given by the format (row, col)
    """
    neighbour = []
    r, c = current
    neighbour.append((r - 1, c))
    neighbour.append((r - 1, c - 1))
    neighbour.append((r - 1, c + 1))
    neighbour.append((r + 1, c))
    neighbour.append((r + 1, c - 1))
    neighbour.append((r + 1, c + 1))
    neighbour.append((r, c - 1))
    neighbour.append((r, c + 1))
    return neighbour


def distances(curr, targets):
    """Return the distance between the target cell and the current position."""
    dist = 0
    import numpy as np
    for point in targets:
        dist += np.sqrt((curr[1] - point[1])**2 + (curr[0] - point[0])**2)
    return dist


def moves(cursor, targets):
    """Move the cursor through the points."""
    if not targets:
        return 0
    currentDist = distances(cursor, targets)
    move = [currentDist]
    for point in neighbours(cursor):
        if distances(point, targets) < currentDist:
            if point in targets:
                move.append(1 + moves(point, targets[:targets.index(point)] +
                                      targets[targets.index(point)+1:]))
            else:
                move.append(1 + moves(point, targets))
    return min(move)


def minimumSteps(points):
    """Try all starting point to find the true minimum way."""
    minSteps = []
    for i, point in enumerate(points):
        minSteps.append(moves(point, points[:1] + points[i+1:]))
    return min(minSteps)


# %%
a = [(0, 0), (1, 1), (1, 2)]
b = [(0, 0), (1, 1), (1, 2), (3, 4)]
# moves((0, 0), [(1, 1), (1, 2), (3, 6)])
minimumSteps(b)
