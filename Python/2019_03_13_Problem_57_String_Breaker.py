#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 13th
# 
# Problem: Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
# 
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
# 
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

# In[11]:


def string_breaker(string, k):                              #
    word = ''                                               # Holder for each word
    cluster = []                                            # Holder for each GROUP of words
    result = []                                             # Final result
    for char in string:                                     # Search each character
        if char != ' ':                                     # If the character is not a space
            word = word + char                              # Add them together to form a word
        else:                                               # If it is a space, anything previous become a word
            if len(word) > k:                               # Then if any word longer than k
                return None                                 # Will render the result null
            if len(' '.join(cluster + [word])) == k:        # If not, then when pasted the previous group and
                result.append(' '.join(cluster + [word]))   # the new word, equal to the requirement
                word = ''                                   # Put the GROUP into the result
                cluster = []                                # And wipe the holders
            elif len(' '.join(cluster + [word])) < k:       # If when pasted, it is still less than k
                cluster.append(word)                        # Add the new word to the group
                word = ''                                   # And wipe the word holder
            else:                                           # If when pasted, it is longer than k
                result.append(' '.join(cluster))            # Add only the group to the result
                cluster = [word]                            # And create a new group
                word = ''                                   # Wipe the word holder
                                                            #
    if cluster:                                             # Then because there is no space at the end
        if len(' '.join(cluster + [word])) <= k:            # Check if there is any available cluster
            result.append(' '.join(cluster + [word]))       # And repeat the same procedure
            word = ''                                       #
        else:                                               #
            result.append(' '.join(cluster))                #
    if word:                                                # Same goes for the word
        result.append(word)                                 #
    return result                                           #


# In[17]:


s = 'the quick brown fox jumps over the lazy dog'
print('The given string is "{}"'.format(s))


# In[18]:


k = int(input('Please choose a limit "k": '))
string_breaker(s, k)

