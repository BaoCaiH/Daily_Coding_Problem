#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 21st
# 
# Problem: Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# 
# For example, given the following matrix:
# 
# `[[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]`
#  
# You should print out the following:
# 
# 1<br>
# 2<br>
# 3<br>
# 4<br>
# 5<br>
# 10<br>
# 15<br>
# 20<br>
# 19<br>
# 18<br>
# 17<br>
# 16<br>
# 11<br>
# 6<br>
# 7<br>
# 8<br>
# 9<br>
# 14<br>
# 13<br>
# 12

# In[69]:


def clockwise_print(matrix):                    #
    n = len(matrix)                             # n_row
    m = len(matrix[0])                          # n_col
    x = 0                                       # col counter
    y = 0                                       # row counter
    while y < n and x < m:                      # While the counters are less than the actual row and col
        for i in range(x, m):                   # Print top row
            print(matrix[y][i], end = ' ')      #
        y += 1                                  #
                                                #
        for i in range(y, n):                   # Print last column
            print(matrix[i][m - 1], end = ' ')  #
        m -= 1                                  #
                                                #
        for i in range(m - 1, x - 1, -1):       # Print last row backward
            print(matrix[n - 1][i], end = ' ')  #
        n -= 1                                  #
                                                #
        for i in range(n - 1, y - 1, -1):       # Print first column backward
            print(matrix[i][x], end = ' ')      #
        x += 1                                  #


# In[70]:


m = [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25],
     [26, 27, 28, 29, 30]]


# In[74]:


print('Given the matrix:')
for row in m:
    print(row)
print('And this is the clockwise printing:')
clockwise_print(m)

