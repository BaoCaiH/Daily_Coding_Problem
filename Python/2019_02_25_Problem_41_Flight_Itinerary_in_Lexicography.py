#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 25th
# 
# Problem: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
# 
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# 
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
# 
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

# In[50]:


def itinerary(flights, start):
    order = []                                                     # The result list
    for i, flight in enumerate(flights):                           # For each flight
        if flight[0] == start:                                     # If the origin matches the given start
            if flights[:i] + flights[i+1:]:                        # Check if there is still flight after this
                next_stop = itinerary(flights[:i] + flights[i+1:], # Loop for the next stop
                                      flight[-1])                  # with a new given start
                if next_stop:                                      # If there is possible order
                    order.append(next_stop)                        # Add it to the possible orders
                else:                                              # Else
                    return None                                    # None all the way
            else:                                                  # If this is the last flight
                order.append([flight[-1]])                         # Return only the destination
    if not order:                                                  # It will check if any path exist
        return None                                                # If one fails, everything fails
                                                                   # This last if statement is effective
                                                                   # only on the first level
    return [start] + min(order)                                    # Return the start + the lexicography smallest order


# In[1]:


l1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
s1 = 'YUL'
l2 = [('SFO', 'COM'), ('COM', 'YYZ')]
s2 = 'COM'
l3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
s3 = 'A'


# In[54]:


print('Given the flights {} and the start airport \'{}\''.format(l1, s1))
print('The flights order is {}'.format(itinerary(l1, s1)))


# In[56]:


print('Given the flights {} and the start airport \'{}\''.format(l2, s2))
print('The flights order is {}'.format(itinerary(l2, s2)))


# In[55]:


print('Given the flights {} and the start airport \'{}\''.format(l3, s3))
print('The flights order is {}'.format(itinerary(l3, s3)))

