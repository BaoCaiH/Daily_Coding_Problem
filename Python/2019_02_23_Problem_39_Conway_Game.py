#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 23rd
# 
# Problem: Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
# 
# >Any live cell with less than two live neighbours dies.<br>
# >Any live cell with two or three live neighbours remains living.<br>
# >Any live cell with more than three live neighbours dies.<br>
# >Any dead cell with exactly three live neighbours becomes a live cell.<br>
# >A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
# 
# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
# 
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
# 
# 

# In[ ]:


0,   1,   2,   3,   4,   5,  '6'
0,   1,   2,   3,   4,   5,  '6'
0,   1,   2,   3,   4,   5,  '6'
0,   1,   2,   3,   4,   5,  '6'
0,   1,   2,   3,   4,   5,  '6'
0,   1,   2,   3,   4,   5,  '6'
'0', '1', '2', '3', '4', '5', '6'


# In[92]:


def rules(row, col, board, height, length):
    '''
    Function to return the living status of the cell given
    '''
    neighbors = []                           # First we list its neighbors
    if row != 0:                             # If it is not the first row
        if col != 0:                         # And if it's not the first column
            neighbors.append((row-1, col-1)) # Add the cell diagonal to the top left
        if col < (length - 1):               # If it's not the last 2 columns,
            neighbors.append((row-1, col+1)) # cause the new board is 1 cell larger on both sides
            neighbors.append((row-1, col))   # Add the cell directly above and diagonally to the top right
        elif col == (length - 1):            # If it is the second last column
            neighbors.append((row-1, col))   # Add the cell directly above
    if row < (height - 1):                   # If it's not the last 2 rows
        if col != 0:                         # if it's not the first column
            neighbors.append((row+1, col-1)) # Add the cell diagonally to the bottom left
        if col < (length - 1):               # and it goes on like above
            neighbors.append((row+1, col+1))
            neighbors.append((row+1, col))
        elif col == (length - 1):
            neighbors.append((row+1, col))
    if col != 0:                             # If it's not the first column
        if row < height:                     # And it is not the last row
            neighbors.append((row, col-1))   # Add the cell directly to the left
    if col < (length - 1):                   # If it's not the last 2 columns
        if row < height:                     # And it is not the last row
            neighbors.append((row, col+1))   # Add the cell directly to the right
    score = 0                                # Time for the scoring
    for i, j in neighbors:                   # Search each neighbor
        if board[i][j] == '*':               # Count the number of living cells in the neighbors
            score += 1
    if row == height or col == length:       # If the cells belong to the new board, naturally it's not living
        if score == 3:                       # If there are exactly 3 living cells nearby
            return '*'                       # Bring it to live
        else:                                # Else
            return '.'                       # Stay dead
    if board[row][col] == '*':               # If the cell in question is living
        if score == 2 or score == 3:         # If the score is between 2 and 3
            return '*'                       # Let it live
        else:                                # Else
            return '.'                       # Kill it
    else:                                    # Same rules for the new cells
        if score == 3:
            return "*"
        else:
            return '.'


# In[103]:


def conway_game(board, step):
    max_row = 0                           # Row and col printing counter
    max_col = 0
    row_dimension = len(board)            # Original row and col
    col_dimension = len(board[0])         # Then create a new board, 1 size larger than the original
    new_board = [['.' for j in range(col_dimension + 1)] for i in range(row_dimension + 1)]
    for x in range(row_dimension + 1):    # For each cell of the new board
        for y in range(col_dimension + 1):# Apply the rule to the cell
            new_board[x][y] = rules(x, y, board, row_dimension, col_dimension)
            if new_board[x][y] == '*':    # If the result is live
                max_row = max(max_row, x) # Check for the new max row and column
                max_col = max(max_col, y) # for printing
    for row in new_board[:max_row+1]:     # Print each row, for niceness
        print(row[:max_col+1])            # Also print enough
    print('')                             # Add 1 line separator
    if step - 1 > 0:                      # If there is still step to play
        conway_game(new_board, step - 1)  # Let's play!


# In[29]:


import random


# In[101]:


b1 = [['*' if random.randint(0, 1) == 1 else '.' for j in range(6)] for i in range(6)]
print('The board below is randomly generated:')
for row in b1:
    print(row)


# In[104]:


step = int(input("How many step do you want to play? Don't make it too long though."))
conway_game(b1, step)

