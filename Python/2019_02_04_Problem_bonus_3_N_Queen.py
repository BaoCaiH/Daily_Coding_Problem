#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 4th
# 
# Problem: You have an N by N board. Write a function that returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

# In[19]:


def n_queen(N, board = []):
    def valid(board):
        current_queen_col, current_queen_row = board[-1], len(board) - 1
        for i in range(len(board) - 1):
            col_diff = abs(current_queen_col - board[i])
            row_diff = abs(current_queen_row - i)
            is_directly_under = (col_diff == 0) # No need checking horizontally because each row only has 1 value
            is_standing_diagonally = (col_diff == row_diff)
            if is_directly_under or is_standing_diagonally:
                return False
        return True
    
    if len(board) == N:                          # If there is only 1 queen left
        return 1                                 # The should only be 1 possible position for it
    arrangement = 0
    for n in range(N):                           # For each column of the first row
        board.append(n)                          # Try put the queen in
        if valid(board):                         # Check if the board is still valid
            arrangement += n_queen(N, board)     # Move on to the next row and repeat
        board.pop()                              # Erase that queen and try other positions
        
    return arrangement


# In[20]:


n_queen(5)

