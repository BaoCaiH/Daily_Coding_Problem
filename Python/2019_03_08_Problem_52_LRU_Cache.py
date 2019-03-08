#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 8th
# 
# Problem: Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
# 
# >set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# 
# >get(key): gets the value at key. If no such key exists, return null.
# 
# Each operation should run in O(1) time.

# In[29]:


class LRU_cache:
    
    def __init__(self, cache_size):                        #
        self.cache_size = cache_size                       # Save the cache size as a permanent element
        self.cache = {}                                    # The actual cache
                                                           #
    def set(self, key, value):                             #
        try:                                               # If the key already exist,
            self.cache.pop(key)                            # remove the current element
        except KeyError:                                   # If not
            if len(self.cache) >= self.cache_size:         # If the capacity is reached
                self.cache.pop(list(self.cache.keys())[0]) # Remove the first element added == least used
        self.cache[key] = value                            # Add a new key and value
                                                           #
    def get(self, key):                                    #
        try:                                               # If the key exist
            value = self.cache.pop(key)                    # Remove key and value from cache and store the value
            self.cache[key] = value                        # Put the key and value at the end of the list
            return value                                   # Return the value
        except KeyError:                                   # If not
            return False                                   # Return false


# In[39]:


print('Create a LRU cache with size of 3')
b = LRU_cache(3)
print('')

print('Give it 3 caches')
b.set(1, 45)
b.set(4, 12)
b.set(5, 9)
print(b.cache)
print('')

print('Use the items a few time so the cache changes a little bit')
b.get(4)
b.get(1)
print(b.cache)
print('')

print('Add a new cache')
b.set(7, 3)
print('See how the least used element disappeared')
print(b.cache)

