#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 9th
# 
# Problem: Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.
# 
# For example, this matrix has 4 islands.
# 
# 1 0 0 0 0<br>
# 0 0 1 1 0<br>
# 0 1 1 0 0<br>
# 0 0 0 0 0<br>
# 1 1 0 0 1<br>
# 1 1 0 0 1

# In[25]:


def findIslands(m):                                 #
    def neighbours(land, m):                        # Supportive function
        neighbour = []                              # To find all the eligible
        h = len(m)                                  # cells that is surrounding the current land
        w = len(m[0])                               # Regardless if it is land or not
        r, c = land                                 #
        if r > 0:                                   #
            neighbour.append((r - 1, c))            #
            if c > 0:                               #
                neighbour.append((r - 1, c - 1))    #
            if c < w - 1:                           #
                neighbour.append((r - 1, c + 1))    #
        if r < h - 1:                               #
            neighbour.append((r + 1, c))            #
            if c > 0:                               #
                neighbour.append((r + 1, c - 1))    #
            if c < w - 1:                           #
                neighbour.append((r + 1, c + 1))    #
        if c > 0:                                   #
            neighbour.append((r, c - 1))            #
        if c < w - 1:                               #
            neighbour.append((r, c + 1))            #
        return neighbour                            #
                                                    #
    lands = []                                      # So find all the lands
    for r in range(len(m)):                         # and put it in a list
        for c in range(len(m[0])):                  #
            if m[r][c] == 1:                        #
                lands.append((r, c))                #
                                                    #
    islands = []                                    # Create a holder for all the island
    for land in lands:                              # For each cell that is land
        if not islands:                             # If there is no island yet
            islands.append([land])                  # Create one for the land
        else:                                       # Otherwise
            cells = neighbours(land, m)             # Find all the neighbouring cells
            tracker = 1                             # And a tracker for that land, 1 land belongs to 1 island
            for cell in cells:                      # For each neighbouring cell
                for i, island in enumerate(islands):# If the cell exists in one of the existing island
                    if cell in island:              #
                        islands[i].append(land)     # Put the land in that island
                        tracker -= 1                # And remove the tracker, like take away an RFID tag
                        break                       # Break the loop, no need to search anymore
                if tracker == 0:                    # If there is no more tracker
                    break                           # Break also the loop for each cell
            if tracker == 1:                        # If after all, the tracker is still there
                islands.append([land])              # It should be a new island, so create one
    return len(islands)                             # Return the number of islands


# In[1]:


m = [[1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]]


# In[27]:


print('Given the map:')
for r in m:
    print(r)


# In[29]:


print('There are {} islands on this map'.format(findIslands(m)))

