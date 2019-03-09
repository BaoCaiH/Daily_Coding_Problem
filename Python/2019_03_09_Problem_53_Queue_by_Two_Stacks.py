#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 8th
# 
# Problem: Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

# In[23]:


# Why the two stacks are needed?
# Maybe it's just the requirement?
class queue:                                            # So the queue
                                                        #
    def __init__(self):                                 # And it has 2 stacks
        self.stack_1 = []                               #
        self.stack_2 = []                               #
                                                        #
    def enqueue(self, insert):                          # Insert the new element in the queue
        self.stack_1.append(insert)                     #
                                                        #
    def dequeue(self):                                  # Removing 
        if not self.stack_1 and not self.stack_2:       # If the stacks are empty
            print('The queue is empty')                 #
            return None                                 #
        if not self.stack_2:                            # If only the second stack is empty
            while self.stack_1:                         # Push element from the first stack, inverted
                self.stack_2.append(self.stack_1.pop()) # Return the last element from the second stack
        return self.stack_2.pop()                       # (aka 1st element ever)


# In[52]:


# # This could do just the same
# # thanks to Python
# class Queue:                            # Meanwhile
#                                         #
#     def __init__(self):                 # The queue
#         self.queue = []                 #
#                                         #
#     def enQueue(self, insert):          # Insert new element
#         self.queue.append(insert)       #
#                                         #
#     def deQueue(self):                  #
#         if not self.queue:              # Certainly if the queue is empty
#             print('The queue is empty') #
#             return None                 #
#         return self.queue.pop(0)        # Otherwise return the first element, by indexing


# In[62]:


FIFO = queue()


# In[63]:


for i in range(3, 9):
    FIFO.enqueue(i)
print(FIFO.stack_1)


# In[64]:


FIFO.enqueue(9)
print(FIFO.stack_1)


# In[65]:


for _ in range(8):
    print(FIFO.dequeue())

