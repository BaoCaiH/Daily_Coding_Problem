#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 7th
# 
# Problem: You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
# 
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
# 
# For example, given the following board:
# 
# `[[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]`
# 
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

# In[172]:


def mininum_steps(board, start, end):
    def possible_step(m, n, start):                       # Sub-function return possible steps
        possible = []                                     # It will return a list
        i, j = start                                      # Current coordinates
        if i - 1 >= 0:                                    # Check whether the adjacent steps are out of
            possible.append((i - 1, j))                   # the board
        if i + 1 < m:                                     # If not, then record the possible step
            possible.append((i + 1, j))
        if j - 1 >= 0:
            possible.append((i, j -1))
        if j + 1 < n:
            possible.append((i, j + 1))
        return possible
    
    def minimum(board, start, end, prev):
        if start == end:                                  # If we are standing on the end point
            return len(prev) - 1, prev                    # Then we don't need to step further
                                                          # The prev parameter includes the start also,
                                                          # that is why -1 is necessary
        m = len(board)                                    # The dimensions of the board is calculated here
        n = len(board[0])
        possibility = possible_step(m, n, start)          # Calculate the possibility
        if end in possibility:                            # If the end point is within the possible moves
            return len(prev), prev + [end]                # We only need to step 1 more step
        min_nsteps = None
        min_steps = None                                  # If it's a normal case, we'll figure out the min
        for i, j in possibility:                          # Take the coordinates of each possibility
            if board[i][j] == 'f' and (i, j) not in prev: # If no wall and not already stepped on
                
                
                # If next STEPS is possible, take only the final value when it reaches the end,
                # means when 1 of the conditions at the beginning is satisfied
                if all(minimum(board, (i, j), end, prev + [(i, j)])):
                    nsteps, steps = minimum(board, (i, j), end, prev + [(i, j)])
                    
                    # Then, if this is the first calculation, assign the result to the min_steps
                    # Otherwise, compare with the existing min value and make changes if necessary
                    if not min_nsteps:
                        min_nsteps = nsteps
                        min_steps = steps
                    elif nsteps < min_nsteps:
                        min_nsteps = nsteps
                        min_steps = steps
        
        return min_nsteps, min_steps
    previous = [start]                                    # Set the start position in the list
    return minimum(board, start, end, previous)


# In[171]:


board = [['f', 'f', 'f', 'f'], ['t', 't', 'f', 't'], ['f', 'f', 'f', 'f'], ['f', 'f', 'f', 'f']]
start = (3, 0)
end = (0, 3)
print('Given the board:')
for row in board:
    print(row)
print('start from {} and end at {}'.format(start, end))


# In[174]:


n_steps, steps = mininum_steps(board, (3, 0), (0, 3))
print('Requires {} step(s) and the steps is/are {}'.format(n_steps, steps))

