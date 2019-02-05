#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 5th
# 
# Problem: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. All flights must be used in the itinerary.
# 
# For example, given the following list of flights:
# 
# HNL ➔ AKL
# 
# YUL ➔ ORD
# 
# ORD ➔ SFO
# 
# SFO ➔ HNL
# 
# and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL.

# In[1]:


flight = [['HNL', 'AKL'], ['YUL', 'ORD'], ['ORD', 'SFO'], ['SFO', 'HNL']]
print(flight)


# In[2]:


def get_itinerary(flights, start):
    def itinerary(flights, start):                          # Sub-function just to get the destination code
        for i, (origin, destination) in enumerate(flights): # Loop through the list
            if origin == start:                             # If the origin matches the assigned start
                return i, destination                       # Return index to pop the list
    flights = flights.copy()                                # So it won't affect the original list
    itinerary_list = [start]                                # First element will be the known start
    while len(flights) > 0:                                 # Until the list is empty
        i, start = itinerary(flights, start)                # Run the sub-function
        itinerary_list.append(start)                        # Put new destination in the list
        flights.pop(i)                                      # Remove the flight
    return itinerary_list


# In[3]:


get_itinerary(flight, 'YUL')


# In[4]:


def get_itinerary(flights, start):
    if len(flights) == 1:                                   # If there is only 1 flight left
        return flights[0]                                   # Obviously we know the origin and destination
    flights = flights.copy()                                # So it won't affect the original list
    itinerary = [start]                                     # First element will be the known start
    for i, (origin, destination) in enumerate(flights):     # Loop through the list
        if origin == start:                                 # If the origin matches the assigned start
            start = destination                             # Assign a new start
            flights.pop(i)                                  # Remove the flight
            itinerary.extend(get_itinerary(flights, start)) # Rerun the function and extend will add the list
    return itinerary                                        # to the original list, ignoring brackets


# In[5]:


get_itinerary(flight, 'YUL')

