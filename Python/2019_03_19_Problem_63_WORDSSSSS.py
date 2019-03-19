#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 19th
# 
# Problem: Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
# 
# For example, given the following matrix:
# 
# `[['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]`
# 
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

# In[6]:


def find_next_char(positions, matrix, chars):                       #
    neighbors = []                                                  # Listing all the neighbors
    m = len(matrix)                                                 # Dimensions of the matrix
    n = len(matrix[0])                                              #
    x = positions[-1][0]                                            #
    y = positions[-1][1]                                            #
    if x > 0:                                                       # Conditions to make sure the indexing is
        neighbors.append((x - 1, y))                                # correct and not out of bound
    if x < m - 1:                                                   #
        neighbors.append((x + 1, y))                                #
    if y > 0:                                                       #
        neighbors.append((x, y - 1))                                #
    if y < n - 1:                                                   #
        neighbors.append((x, y + 1))                                #
    if len(chars) == 1:                                             # If there is only 1 character left
        for i, j in neighbors:                                      # If it's not one of the neighbor
            if matrix[i][j] == chars and (i, j) not in positions:   # Then return None
                return positions + [(i, j)]                         # Otherwise, return its position
        return None                                                 #
    for i, j in neighbors:                                          # If there are more than 1 character
        if matrix[i][j] == chars[0] and (i, j) not in positions:    # Find it in the neighbor
            next_positions = find_next_char(positions + [(i, j)], matrix, chars[1:]) # And recurse the problem
            if next_positions:                                      # If the result is not None
                return next_positions                               # Add it to the positions list
    return None                                                     # If it is None, return None then
                                                                    #
def find_word(matrix, word):                                        # The main function job is to find
    for i, row in enumerate(matrix):                                # the first character position
        for j, char in enumerate(row):                              #
            if char == word[0]:                                     # Then the other function will handle
                next_positions = find_next_char([(i, j)], matrix, word[1:])# the rest
                if next_positions:                                  # Same drill, if the result is not None
                    return next_positions                           # then return the position list
    print('The word "{}" cannot be found in this matrix'.format(word)) # If not then throw an error
    return None                                                        # Return nothing


# In[3]:


m = [['F', 'A', 'C', 'T'],
     ['O', 'B', 'A', 'P'],
     ['A', 'S', 'S', 'E'],
     ['M', 'N', 'O', 'T']]


# In[25]:


print('Given the matrix below:')
for row in m:
    print(row)


# In[13]:


import time
print('The word "FACT" has the following character positions: {}'.format(find_word(m, 'FACT')))
print('The word "BASS" has the following character positions: {}'.format(find_word(m, 'BASS')))
print('The word "NOTE" has the following character positions: {}'.format(find_word(m, 'NOTE')))
print('The word "NOSE" has the following character positions: {}'.format(find_word(m, 'NOSE')))
print('The word "ASSET" has the following character positions: {}'.format(find_word(m, 'ASSET')))
print('The word "BASE" has the following character positions: {}'.format(find_word(m, 'BASE')))
print('The word "BASSS" has the following character positions: {}'.format(find_word(m, 'BASSS')))
time.sleep(1)
print('Ha!')

