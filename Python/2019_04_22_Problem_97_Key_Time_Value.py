#!/usr/bin/env python
# coding: utf-8
"""2019 April 22th - Daily_Coding_Problem #97."""
# <markdown>
# ## 2019 April 22th - Daily_Coding_Problem #97
#
# Problem: Write a map implementation with a get function that lets you
# retrieve the value of a key at a particular time.
#
# It should contain the following methods:
#
# `set(key, value, time)`: sets key to value for `t = time`.
# `get(key, time)`: gets the key at `t = time`.
# The map should work like this. If we set a key at a particular time,
# it will maintain that value forever or until it gets set at a later time.
# In other words, when we get a key at a time,
# it should return the value that was set for that
# key set at the most recent time.
#
# Consider the following examples:
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
#
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2


# <codecell>
class Map:
    """Storing class of the map."""

    def __init__(self):
        """Initialize the holding dictionary."""
        self.dict = {}

    def set(self, key, value, time):
        """Set the value based on key and time."""
        if key not in self.dict:
            self.dict[key] = {}
        self.dict[key][time] = value

    def get(self, key, time):
        """Get the value given the key and time."""
        if key not in self.dict:
            print('The given key has not been registered')
            return None
        storage = None
        for t, v in self.dict[key].items():
            if t < time:
                storage = v
            elif t == time:
                return v
            else:
                return storage
        return storage


# %%
m = Map()

m.set(1, 9, 0)
m.set(1, 10, 2)
print(m.get(1, 1))
print(m.get(1, 3))

# %%
m = Map()

m.set(1, 1, 5)
print(m.get(1, 0))
print(m.get(1, 10))

# %%
m = Map()

m.set(1, 1, 0)
m.set(1, 19, 0)
print(m.get(1, 0))
