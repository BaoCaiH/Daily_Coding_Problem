#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 10th
# 
# Problem: Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
# 
# Implement an efficient sudoku solver.

# In[70]:


def complete(board):                                    # Supportive function, check if completed
    for row in board:                                   # Search each cells from each row
        for cell in row:                                #
            if cell == 0:                               # If any call is not filled
                return False                            # It's not solved
    return True                                         # Othewise, yes
                                                        #
def find_an_empty_cell(board):                          # Supportive function, find an empty cell
    for i, row in enumerate(board):                     # Similar to above
        for j, cell in enumerate(row):                  #
            if cell == 0:                               # But return the coordinates when found any empty cell
                return i, j                             #
                                                        #
def duplicates(array):                                  # Supportive function, duplicate is the deal breaker
    holder = []                                         # A value holder
    for val in array:                                   # Given any array, may it be row, col or 3 by 3 block
        if val != 0:                                    # If it is not empty
            if val in holder:                           # If is in the holder
                return True                             # Immediately return True on duplicate
            holder.append(val)                          # If not, add to the holder
    return False                                        # In the end, false
                                                        #
def all_rows_are_valid(board):                          # Supportive function, check every row for validity
    for row in board:                                   # Feed each row to the duplicates function
        if duplicates(row):                             # If any row fail the test
            return False                                # Return False on validity
    return True                                         # Otherwise, True
                                                        #
def all_cols_are_valid(board):                          # Supportive function, check every column for validity
    for j in range(9):                                  # For each column
        if duplicates([board[i][j] for i in range(9)]): # Feed it to the duplicates by list comprehence
            return False                                # If fail, False
    return True                                         # Otherwise, True
                                                        #
def all_blocks_are_valid(board):                        # Supportive function, check every 3 by 3 block
    for i in range(0, 9, 3):                            # Blocks are 3 cells apart from each other
        for j in range(0, 9, 3):                        # In both row and column
            block = []                                  # Value holder
            for k in range(3):                          # Each block is 3 cell wide
                for l in range(3):                      # and heigh
                    block.append(board[i+k][j+l])       # Put the value into the holder
            if duplicates(block):                       # Then feed it to the duplicates function
                return False                            # If fail, False
    return True                                         # Otherwise, True
                                                        #
def board_is_valid(board):                              # Supportive function, overall validity check
    if not all_rows_are_valid(board):                   # Check the rows
        return False                                    #
    if not all_cols_are_valid(board):                   # Then columns, any order is fine, really
        return False                                    #
    if not all_blocks_are_valid(board):                 # Finally, blocks
        return False                                    #
    return True                                         #
                                                        #
def sudoku_solver(board):                               # Main function
                                                        #
    if complete(board):                                 # If the board is already completed
        return board                                    # Return it
                                                        #
    row, col = find_an_empty_cell(board)                # If not then find a cell that is empty
                                                        #
    for value in range(1, 10):                          # Try every value
        board[row][col] = value                         #
        if board_is_valid(board):                       # If the board is still valid after try in
            result = sudoku_solver(board)               # Continue to the next cell
        if complete(board):                             # After that, if the board is completed
            return result                               # Return it
        board[row][col] = 0                             # Else, change the cell back to empty and re-do


# In[71]:


sudoku_board = [[0, 6, 0, 0, 0, 3, 0, 0, 7],
               [3, 0, 0, 6, 8, 0, 0, 1, 0],
               [1, 9, 0, 2, 0, 0, 0, 0, 0],
               [6, 8, 5, 0, 0, 0, 1, 3, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [2, 1, 0, 0, 0, 0, 0, 0, 0],
               [4, 0, 3, 0, 0, 0, 0, 0, 6],
               [0, 0, 0, 0, 2, 0, 0, 0, 9],
               [0, 0, 0, 0, 4, 0, 8, 7, 0]]


# In[ ]:


print('A hard-level board is given below:')


# In[72]:


for i in range(9):
    if i in [0, 3, 6]:
        print('-------------------')
    for j in range(9):
        if j in [0, 3, 6]:
            print('|', end = '')
        print(sudoku_board[i][j], end = '')
        if j not in [2, 5, 8]:
            print(' ', end = '')
    print('|')
print('-------------------')


# In[73]:


import datetime
a = datetime.datetime.now()
solved_board = sudoku_solver(sudoku_board)
b = datetime.datetime.now()


# In[82]:


print('The solved board is as below and it is solved in {} seconds'.format((b.second - a.second)))


# In[74]:


for i in range(9):
    if i in [0, 3, 6]:
        print('-------------------')
    for j in range(9):
        if j in [0, 3, 6]:
            print('|', end = '')
        print(solved_board[i][j], end = '')
        if j not in [2, 5, 8]:
            print(' ', end = '')
    print('|')
print('-------------------')

