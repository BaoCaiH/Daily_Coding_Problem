#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 3rd
# 
# Problem: A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# 
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

# In[1]:


def generate_matrix(n_row, k_col):
    import random
    matrix = []
    for n in range(n_row):
        row = [random.randint(1, 100) for k in range(k_col)]
        matrix.append(row)
    return matrix


# In[2]:


m = generate_matrix(5, 3)


# In[3]:


print('Given a random cost matrix below:')
for i in m:
    print(i)


# In[4]:


def min_matrix_cost(matrix):
    '''
    Accept a matrix in nested list form
    Return a list of minimum cost and a sub-list of the path taken leading to that cost
    '''
    N = len(matrix)
    K = len(matrix[0])
    # Create an empty holder for cummulative costs after each layer
    cummulative_cost = [[[0, []] for _ in range(K)] for i in range(N)]
    # For every position
    for n in range(N):
        for k in range(K):
            # Check all the possible previous path leading to that point to find the min
            # Without repeating a column, excluding k
            # The first layer will be a dummy since it reference the last layer, which is empty at first
            previous_cummulative_cost = cummulative_cost[n - 1][:k] + cummulative_cost[n - 1][k + 1:]
            previous_min = min(previous_cummulative_cost)
            previous_index = cummulative_cost[n - 1].index(previous_min)
            # Deep copy is required here, or else it will be extensive when the original value is changed
            previous_path = cummulative_cost[n - 1][previous_index][-1].copy()
            # Create a list of path
            previous_path.append(previous_index)
            # Assign the current min value
            cummulative_cost[n][k][0] = matrix[n][k] + previous_min[0]
            # Assign the current path
            cummulative_cost[n][k][-1] = previous_path
            # If this is the last layer
            if n == N - 1:
                # Remove the unecessary first dummy layer
                cummulative_cost[n][k][-1] = cummulative_cost[n][k][-1][1:]
                # Append the last layer positions
                cummulative_cost[n][k][-1].append(k)
    min_cost, path_0 = min(cummulative_cost[-1])
    path = [matrix[i][path_0[i]] for i in range(len(path_0))]
    return min_cost, path


# In[5]:


min_cost, path = min_matrix_cost(m)


# In[6]:


print('The minimum cost is {}'.format(min_cost))
print('The path leading toward that is {}'.format(path))

