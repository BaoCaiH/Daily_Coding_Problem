#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 3rd
# 
# Problem: Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

# In[153]:


class Node:                                                             # Class to holder the linked list values
    def __init__(self, value):                                          #
        self.value = value                                              #
        self.next = None                                                #
                                                                        #
class singly_linked_list:                                               # The linked list
    def __init__(self):                                                 # The items will be added in reverse
        self.head = None                                                # ironically, because Python doesn't have
                                                                        # a pointer
    def add_item(self, value):                                          # Add new item
        node = Node(value)                                              # Give it the value
        node.next = self.head                                           # Point the next value to value in front
        self.head = node                                                # Expose the head of the list
                                                                        #
    def print_list(self):                                               # Printing items
        printing = self.head                                            # Because items are added in reverse
        while printing:                                                 # The last item is actually the first
            print(printing.value, end = ' ')                            # Print the first value
            printing = printing.next                                    # And use the next pointer to move forward
        print('')                                                       #
                                                                        #
    def reverse(self):                                                  # Reversing
        prev = None                                                     # The end of the list is None, like 'init'
        current = self.head                                             # Start from the head like printing
        while current is not None:                                      # Swap the pointers, Next becomes Previous
             current.next, prev, current = prev, current, current.next  # Prev and Current are just holders
        self.head = prev                                                # Move them along the list
        
############################# Up to this point, it is to setup the singly linked list ############################
        
def merge_k_singly_linked_list(kLst):                           #
    k = len(kLst)                                               # Find k
    kLst = kLst.copy()                                          # Take a copy, so it won't change the original lst
    for i in range(k):                                          # Start at the head of each list
        kLst[i] = kLst[i].head                                  #
    tray = []                                                   # Get all the first values into a heap list
    heapq.heapify(tray)                                         # They are all minimum from each list
    for e in kLst:                                              #
        heapq.heappush(tray, e.value)                           #
    merged = singly_linked_list()                               #
    while tray:                                                 # While the tray still has at least an element
        adding = heapq.heappop(tray)                            # Take the min element
        for i in range(k):                                      # Through each list
            if kLst[i] is not None and kLst[i].value == adding: # If the current head is not None and equal to min
                merged.add_item(adding)                         # Add it to the merged list
                kLst[i] = kLst[i].next                          # Then move to the next element in that list
                if kLst[i] is not None:                         # If the new element is not None
                    heapq.heappush(tray, kLst[i].value)         # Add new value to the heap list
                break                                           #
    merged.reverse()                                            # Reverse to become an ascending list
    merged.print_list()                                         #


# In[111]:


l1 = singly_linked_list()
l2 = singly_linked_list()
l3 = singly_linked_list()


# In[112]:


l1.add_item(7)
l1.add_item(5)
l1.add_item(3)
l1.add_item(1)

l2.add_item(8)
l2.add_item(6)
l2.add_item(4)
l2.add_item(2)

l3.add_item(11)
l3.add_item(10)
l3.add_item(9)
l3.add_item(0)


# In[156]:


k = [l1, l2, l3]
print('Given the 3 sorted list:')
for e in k:
    e.print_list()


# In[157]:


print('Merge them:')
merge_k_singly_linked_list(k)

