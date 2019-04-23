#!/usr/bin/env python
# coding: utf-8
"""2019 April 23th - Daily_Coding_Problem #98."""
# <markdown>
# ## 2019 April 23th - Daily_Coding_Problem #98
#
# Problem: Given a 2D board of characters and a word,
# find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example, given the following board:
#
# `[
# ['A','B','C','E'],
# ['S','F','C','S'],
# ['A','D','E','E']
# ]`
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true,
# exists(board, "ABCB") returns false.


# <codecell>
def neighbours(current, sizes):
    """Return the neighbouring cells."""
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


# %%
def exists(board, word, positions=[]):
    """Find the given word in the board."""
    if not word:
        return positions
    h = len(board)
    w = len(board[0])
    if positions:
        neighbour = neighbours(positions[-1], (h, w))
        for (r, c) in neighbour:
            if (r, c) not in positions and word[0] == board[r][c]:
                path = exists(board, word[1:], positions + [(r, c)])
                if path:
                    return path
        return None

    for r in range(h):
        for c in range(w):
            if word[0] == board[r][c]:
                path = exists(board, word[1:], positions + [(r, c)])
                if path:
                    return path
    return False


# %%
board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
exists(board, "ABCCED")
