#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 21st - bonus
# 
# Problem: return a new sorted merged list from K sorted lists, each with size N

# In[1]:


list_1 = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
list_2 = []
list_3 = [[], [1], [1,2]]
list_4 = [[1]]
list_5 = [[1], [1, 3, 5], [1, 10, 20, 30, 40]]


# In[57]:


# This method use only list and base python
def merge_lists_just_list(lists):
    merged_list = []
    for lst in lists:                   # Take each list
        for element in lst:             # View each element in the respective list
            merged_list.append(element) # Put it in the merged
    merged_list.sort()                  # Sort it
    return merged_list                  # Done


# In[60]:


# This method use heap, suggested by Marc from DailyCodingProblem
# Heap is a binary tree where parent nodes are less than their children
# I learnt this and modified so I can understand better
def merge_lists_heap(lists):
    import heapq                                                 # We need to import heapq
    merged_list = []                                             # Prepared an empty list
    heap = []                                                    # Also one for heap
    for i, lst in enumerate(lists):                              # We can also substitute i by calling index later
        if lst:                                                  # If the inside list exist, not empty
            heap.append((lst[0], i, 0))                          # Each element of heap will have the value itself, which list it belongs to, and which element in the list
    heapq.heapify(heap)                                          # At this point, only the first element of each list is in the heap, other elements will be added later    
    while heap:                                                  # So while the heap is still exist, not empty. We will slowly delete the heap during the loops
        element, list_index, element_index = heapq.heappop(heap) # Each heap has 3 values so take it out. heappop will take out and delete the smallest element in the heaps
        merged_list.append(element)                              # Because the element in the heap is sorted automatically, we immediately add the taken out element to the merged list
        if element_index + 1 < len(lists[list_index]):           # Add a new heap element if the value we just used is not the last element of its respective list
            new_element = (lists[list_index][element_index + 1], # So add 1 unit of element index accordingly
                          list_index,                            # Also the new element will be automatically sorted
                          element_index + 1)
            heapq.heappush(heap, new_element)                    # Add the new heap element here and continue looping
    return merged_list                                           # Finish


# In[62]:


import datetime as dt


# In[103]:


print('There are 2 methods in this problem\nOne use heap and the one use just the list and base python\nWe can benchmark them to see which one solve the question the best')
a = dt.datetime.now()
x = merge_lists_heap(list_5)
b = dt.datetime.now()
y = merge_lists_just_list(list_5)
c = dt.datetime.now()
print('Given the original list is {}\nThe results from heap and just_list respective are\n{}\n{}'.format(list_5, x, y))
e = {'heap' : b - a,
    'just_list' : c - b}
print(e)
print('Which one is faster?')

