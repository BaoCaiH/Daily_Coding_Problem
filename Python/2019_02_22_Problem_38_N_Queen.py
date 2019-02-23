#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 2nd
# 
# Problem: You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
# 
# >This is the same as the bonus problem number 3 posted previously, re-did it, might be slightly different, work either ways

# In[11]:


def n_queen(N, board = []):
    
    def valid(board):                                                    # After adding queens by each row
        current_queen_col, current_queen_row = board[-1], len(board) - 1 # Take the last row position
        for row in range(len(board) - 1):                                # Then compare to the previous rows
            col_distance = abs(current_queen_col - board[row])           # Compare if they are at the same col
            row_distance = abs(current_queen_row - row)                  # How far away, in rows
            is_directly_under = col_distance == 0
            is_standing_diagonally = col_distance == row_distance
            if any([is_directly_under, is_standing_diagonally]):         # If any is true
                return False                                             # That position is not valid
        return True                                                      # Else, true
    
    if len(board) == N:                                                  # If the board is already filled
        return 1                                                         # Only one possible arrangement
    arrangement = 0                                                      # Else, start at 0
    for column in range(N):                                              # On each position on each row,
        board.append(column)                                             # Place the queen
        if valid(board):                                                 # If it's valid
            arrangement += n_queen(N, board)                             # Move on to the next row
        board.pop()                                                      # Then remove it, and change position
    return arrangement                                                   # Return the total sum


# In[10]:


n_queen(5)

