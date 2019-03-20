#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 20th
# 
# Problem: A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
# 
# Given N, write a function to return the number of knight's tours on an N by N chessboard.

# In[ ]:


def possible_moves(N, board, start):
    tours = 0
    moves = []
    x = start[0]
    y = start[1]
    if x >= 2:
        if y >= 1:
            if board[x - 2][y - 1] != 1:
                moves.append((x - 2, y - 1))
        if y <= N - 2:
            if board[x - 2][y + 1] != 1:
                moves.append((x - 2, y + 1))
    if x <= N - 3:
        if y >= 1:
            if board[x + 2][y - 1] != 1:
                moves.append((x + 2, y - 1))
        if y <= N - 2:
            if board[x + 2][y + 1] != 1:
                moves.append((x + 2, y + 1))
    if y >= 2:
        if x >= 1:
            if board[x - 1][y - 2] != 1:
                moves.append((x - 1, y - 2))
        if x <= N - 2:
            if board[x + 1][y - 2] != 1:
                moves.append((x + 1, y - 2))
    if y <= N - 3:
        if x >= 1:
            if board[x - 1][y + 2] != 1:
                moves.append((x - 1, y + 2))
        if x <= N - 2:
            if board[x + 1][y + 2] != 1:
                moves.append((x + 1, y + 2))
    return moves

def knight_moves(N, board, lst):
    if len(lst) == N * N:
        return 1
    tours = 0
    moves = possible_moves(N, board, lst[-1])
    if not moves:
        return 0
    for i, j in moves:
        lst.append((i, j))
        board[i][j] = 1
        tours += knight_moves(N, board, lst)
        board[i][j] = 0
        lst.pop()
    return tours

def knight_tours(N):
    tours = 0
    for i in range(N):
        for j in range(N):
            board = [[0 for _ in range(N)] for _ in range(N)]
            board[i][j] = 1
            tours += knight_moves(N, board, [(i, j)])
    return tours


# In[11]:


run = input("It's going to take a long time to run, do you want to continue (N/y)")
if run != 'y':
    run = "N"
if run == 'y':
    knight_tours(5)

