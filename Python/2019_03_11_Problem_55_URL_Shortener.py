#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 11th
# 
# Problem: Implement a URL shortener with the following methods:
# 
# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
# 
# Hint: What if we enter the same URL twice?

# In[77]:


class url_database:
    
    # We need a database, with ids, urls and the shorten version
    # Plus all the characters that can be used in the shorten url
    def __init__(self):
        self.id = []
        self.urls = []
        self.shorten_urls = []
        self.alphameric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def generate_id(self):                                          # Supportive function to create unique ids
        import random                                               #
        temp_id = int(10**10 * random.random())                     # We need a 10 digits id
        if temp_id not in self.id:                                  # to create 6 chars short url
            return temp_id                                          # Also check if this id already existed
        return generate_id()                                        #
                                                                    #
    def shorten(self, url):                                         # Shorten function
        try:                                                        # Try to find if the url already existed
            return ''.join(self.shorten_urls[self.urls.index(url)]) # And return the shorten version
        except ValueError:                                          # If not
            short = []                                              # Create a holder
            new_id = self.generate_id()                             # Generate a new id
            self.id.append(new_id)                                  # And put it in the id list
            while new_id > 0:                                       # Turn decimal-number id into base-62 string
                short.append(self.alphameric[new_id % 62])          # Mathematics at this point only
                new_id = new_id // 62                               #
            self.urls.append(url)                                   # Store the new url
            self.shorten_urls.append(short)                         # And the shorten as well
            return ''.join(short)                                   # Paste all the chars in the short and return
                                                                    #
    def restore(self, short):                                       # Restore function
        find_id = 0                                                 # Restore the id
        for i, char in enumerate(short):                            # Also math
            find_id += self.alphameric.index(char) * 62**i          #
        try:                                                        # Then try and find the id in the list
            return self.urls[self.id.index(find_id)]                # Return the original url if exist
        except ValueError:                                          # Else
            print('The shorten URL does not exist')                 # Throw an error
            return None                                             # Return nothing


# In[82]:


urls = url_database()
original_url = 'BaoCaiH/Daily_Coding_Problem'
print('Given the original url extension to my github repository \'{}\''.format(original_url))


# In[83]:


short_url = urls.shorten(original_url)
print('After shorten, it is represented as \'{}\''.format(short_url))


# In[84]:


print('Restored: {}'.format(urls.restore(short_url)))

