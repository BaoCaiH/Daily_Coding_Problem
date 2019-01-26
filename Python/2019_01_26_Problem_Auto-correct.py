#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 26th
# 
# Problem: Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# 
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# 
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

# In[23]:


def autocomplete(string, possible_query):
    
    def dictionary(possible_query):
        dictionary = {}
        for query in possible_query:
            if query[0] not in dictionary:
                dictionary[query[0]] = []
            dictionary[query[0]].append(query)
        return dictionary
    
    dct = dictionary(possible_query)
    
    dct = dct[string[0].lower()]
    
    return [wrd for wrd in dct if wrd.lower().startswith(string.lower())]


# In[59]:


import pandas as pd
dic = pd.read_csv('english-word-list-total.csv', skiprows = 3, header = 0, sep = ';')
dicts = [wrd for wrd in dic['word']]
dicts = dicts[:500]


# In[62]:


s = input('Type some prefix: ')
autocomplete(s, dicts)

