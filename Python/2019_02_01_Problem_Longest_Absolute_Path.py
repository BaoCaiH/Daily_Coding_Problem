#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 1st
# 
# Problem: Suppose we represent our file system by a string in the following manner:
# 
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# 
# `dir
#     subdir1
#     subdir2
#         file.ext`
#         
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# 
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# 
# `dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext`
#             
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# 
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# 
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
# 
# Note:
# 
# The name of a file contains at least a period and an extension.
# 
# The name of a directory or sub-directory will not contain a period.

# In[161]:


st = ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

st2 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' +'\ndir2\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\t\t\tsubsubsubdir3\n\t\t\t\tfile3.ext'


# In[153]:


def longest_absolute_path(file_system):
    
    def check_level(path):                                       # A separate function to count indentation
        n_tab = 0                                                # First set the default indentation at 0
        while path.startswith('\t'):                             # For every tab it found
            path = path[1:]                                      # Remove the tab
            n_tab += 1                                           # And count the tabs
        return n_tab, path                                       # Return the number of tab + the path
                                                                 # without the tabs
    absolute_list = []                                           # Create empty list to store the paths
    absolute_path = ''                                           # And empty string for comparison
    for branch in file_system.split('\n'):                       # Treat every line as a path
        level, branch = check_level(branch)                      # Apply the level counting function
        if level == len(absolute_list):                          # If the level equal to the number of element in the list,
            absolute_list.append(branch)                         # then the new item will be the new level
        elif level < len(absolute_list):                         # If less, it means either there are more than 1 file/dir in this level
                                                                 # or this (sub)dir is fully checked
            absolute_list = absolute_list[:level]                # Erase the list upto the level we need
            absolute_list.append(branch)                         # Add the new element
        if '.' in absolute_list[-1]:                             # Before looping, if the last item is a file
            if len('/'.join(absolute_list)) > len(absolute_path):# If the current path is longer than the stored path
                absolute_path = '/'.join(absolute_list)          # Replace the path then continue looping
                                                                 # It will store the path here so the erase step above
                                                                 # will not affect the past elements (took me a while to understand)
    return absolute_path


# In[163]:


print('Given the path:')
print(st)
lst = longest_absolute_path(st)
print('The longest absolute path is {},\n and it is {} characters long'.format(lst, len(lst)))


# In[164]:


print('Given the path:')
print(st2)
lst2 = longest_absolute_path(st2)
print('The longest absolute path is {},\n and it is {} characters long'.format(lst2, len(lst2)))

