#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 29th
# 
# Problem: Given the head of a singly linked list, reverse it in-place

# In[1]:


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


# In[2]:


l = singly_linked_list()
l.add_item(20)
l.add_item(30)
l.add_item(40)
l.add_item(50)
l.add_item(60)


# In[3]:


l.print_list()


# In[4]:


l.reverse()


# In[5]:


l.print_list()

