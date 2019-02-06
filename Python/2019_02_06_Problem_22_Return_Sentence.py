#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 6th
# 
# Problem: Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# 
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# 
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

# In[130]:


def return_sentence(string, lst):
    sets = []                                                   # First a set to store the results
    for i in lst:                                               # For each word in the list
        if string.startswith(i):                                # If the string starts with the word
            sets.append(i)                                      # Put that word in the list
            if string[len(i):]:                                 # If the string continues after that word
                subsets = return_sentence(string[len(i):], lst) # Re-run the function
                if subsets:                                     # If it does return something
                    sets.extend(subsets)                        # Put the sub-results in the results
                    break                                       # And stop looping, because we got it
                else:                                           # Else, anything goes wrong toward the end
                    sets.pop()                                  # Render the list empty and start over
    if sets:                                                    # If the results available
        return sets                                             # Return it
    else:                                                       # If not
        return None                                             # Return None


# In[112]:


s1 = 'thequickbrownfox'
lst1 = ['quick', 'brown', 'the', 'fox']


# In[114]:


s2 = "bedbathandbeyond"
lst2 = ['bed', 'bath', 'bedbat', 'hand', 'beyond']


# In[115]:


s3 = "bedbathandbeyond"
lst3 = ['bed', 'bedbat', 'and', 'beyond']


# In[134]:


print('Given the string \'{}\' and the list of words {}'.format(s1, lst1))
print('The sentence is: {}'.format(return_sentence(s1, lst1)))


# In[135]:


print('Given the string \'{}\' and the list of words {}'.format(s2, lst2))
print('The sentence is: {}'.format(return_sentence(s2, lst2)))


# In[136]:


print('Given the string \'{}\' and the list of words {}'.format(s3, lst3))
print('The sentence is: {}'.format(return_sentence(s3, lst3)))

