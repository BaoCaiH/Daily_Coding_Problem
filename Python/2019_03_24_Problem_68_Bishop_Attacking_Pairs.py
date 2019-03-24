#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 24th
# 
# Problem: On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
# 
# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
# 
# For example, given M = 5 and the list of bishops:
# 
# (0, 0)<br>
# (1, 2)<br>
# (2, 2)<br>
# (4, 0)
# 
# The board would look like this:
# 
# `[b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]`
# 
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

# In[18]:


def bishop_attacking_pairs(N, M, count = True):                             #
    last = len(N)                                                           # Count the number of bishop
    attack_pairs = []                                                       # Storage for the pairs
    for i, bishop in enumerate(N):                                          # For each bishop
        if i == last - 1:                                                   # Skip the last bishop
            break                                                           # Because order is not important
        if not (bishop[0] >= M or bishop[1] >= M):                          # Skip those outside the board
            for another_bishop in N[i+1:]:                                  # Search other bishops
                if not (another_bishop[0] >= M or another_bishop[1] >= M):  # Also skip those outside the board
                    if abs(bishop[0] - another_bishop[0]) ==                        abs(bishop[1] - another_bishop[1]):                 # If they are diagonal from each other
                        attack_pairs.append((bishop, another_bishop))       # Add the pair
    if count is True:                                                       # Return the number of the pairs
        return len(attack_pairs)                                            #
    return attack_pairs                                                     # Or the pairs themselves


# In[19]:


lst = [(0, 0), (1, 2), (2, 2), (4, 0)]
print('Given the 5 by 5 board and the following bishops: {}'.format(lst))
print('There are {} pairs of bishops attacking one another'.format(bishop_attacking_pairs(lst, 5)))

