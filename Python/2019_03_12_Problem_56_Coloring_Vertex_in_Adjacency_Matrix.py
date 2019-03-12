#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 12th
# 
# Problem: Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

# In[43]:


def coloring(m, k, result = 'colorability'):        #
    colors = []                                     # Holder for each vertexes' color
    for i, v in enumerate(m):                       # For each vertex
        if not colors:                              # If the holder is empty (only happen at the beginning)
            colors.append(i)                        # Put the first color in, aka. color 0
                                                    #
        else:                                       # Otherwise
            exceptions = []                         # Create an exception colors cannot be used on this vertex
            for j, w in enumerate(v):               # Search the adjacency
                if w == 1:                          # If they are neighbors
                    try:                            # And the neighbors were previously assigned a color
                        exceptions.append(colors[j])# Add their colors to the exception
                    except IndexError:              # If they have yet have a color
                        break                       # Don't do anything
            choices = [color for color in colors\   # Choices are colors which has not been used
                       if color not in exceptions]  # aka. not in exception
            if not choices:                         # If the choices are empty
                colors.append(max(colors) + 1)      # Add a new color
            else:                                   # Else
                colors.append(min(choices))         # Use the first color available
                                                    #
    unique_colors = []                              #
    for color in colors:                            # Colors used can be duplicated so
        if color not in unique_colors:              # This is to find the unique colors
            unique_colors.append(color)             #
                                                    # This part is outside the question
    if result == 'colorability':                    # If you interested in answering the question of quantity
        return len(unique_colors) <= k              # Compare with the given k
    elif result == 'vertex colors':                 # If interested in which color on which vertex
        return colors                               # Choose this option and return colors
    elif result == 'unique colors':                 # If interested in unique colors
        return unique_colors                        # Choose this option
    else:
        print('The argument result only has 3 possibilities and \'{}\' is not one of them.'.format(result))
        print("Please choose one among 'colorability', 'vertex colors' and 'unique colors'")
        return None


# In[45]:


m = [[0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]]
k = 3


# In[46]:


print('Given the adjacency matrix below and {} colors:'.format(k))
for v in m:
    print(v)
print('Will the {} colors suffice to color the vertexes? {}'.format(k, coloring(m, k)))
print('These are the unique colors: {}'.format(coloring(m, k, result = 'unique colors')))
print('This is how the vertexes are colored: {}'.format(coloring(m, k, result = 'vertex colors')))

