#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 28th
# 
# Problem: In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
# 
# Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.
# 
# The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.
# 
# For example, the following input graph:
# 
# ABACA<br>
# [(0, 1),<br>
#  (0, 2),<br>
#  (2, 3),<br>
#  (3, 4)]
# 
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
# 
# The following input graph:
# 
# A<br>
# [(0, 0)]
# 
# Should return null, since we have an infinite loop.

# In[68]:


def find_path(path, remaining):                                           # Supporting function
    if len(remaining) == 0:                                               # If there is no other nodes
        return [path]                                                     # Return the last end
    paths = [path]                                                        # Otherwise create a holder
    for i, node in enumerate(remaining):                                  # For each node
        if node[0] == path[-1]:                                           # If the last end matches the node start
            paths = paths + [path + case for case in find_path([node[1]], # Re-run the function for the remaining
                                    remaining[:i] + remaining[i+1:])]     # nodes. Treat results as possibility
    return paths                                                          #
                                                                          #
def has_duplicate(path):                                                  # Supporting function
    tmp = []                                                              # To check if the path is an infinite loop
    for node in path:                                                     #
        if node not in tmp:                                               #
            tmp.append(node)                                              #
        else:                                                             #
            return True                                                   #
    return False                                                          #
                                                                          #
def mode_on_path(s, p):                                                   # Main function
    possible_paths = []                                                   # Holder, similar to the first support
    for i, node in enumerate(p):                                          # Run the first step of the support
        possible_paths = possible_paths + find_path([node[0], node[1]],   # function on each node
                                                       p[:i] + p[i+1:])   #
    modes = []                                                            # Holder for the modes of each path
    for path in possible_paths:                                           # For each path
        if not has_duplicate(path):                                       # That is not an infinite loop
            dictionary_temp = {}                                          # Create a dictionary for counting
            for node in path:                                             # Check each node
                if s[node] not in dictionary_temp:                        # If the node is not yet in dictionary
                    dictionary_temp[s[node]] = 0                          # Add it in
                dictionary_temp[s[node]] += 1                             # Increase the value
            modes.append(max(dictionary_temp.values()))                   # Add the max to the modes
        else:                                                             # If the path is looped infinitely
            modes.append(None)                                            # Add None
    return max(modes)                                                     # Then find the max among the Modes


# In[60]:


s = "ABACA"
p_1 = [(0, 1), (0, 2), (2, 3), (3, 4)]
p_2 = [(0, 0)]


# In[71]:


print('Given the graph "{}" and the paths {}. The largest value path is {}'.format(s, p_1, mode_on_path(s, p_1)))

