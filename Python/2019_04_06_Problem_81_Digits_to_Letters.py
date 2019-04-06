#!/usr/bin/env python
# coding: utf-8

# ## 2019 April 6th
# 
# Problem: Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
# 
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

# In[23]:


def digitsToLeters(digitString, digitsMap):             #
    if digitString[0] not in digitsMap:                 # Give a warning for wrong input(s)
        print('This digit "{}" is not available in the digit map.'.format(digitString[0]))
        print('The digits should be those in this list: {}'.format(digitsMap.keys()))
        return None                                     #
    if len(digitString) == 1:                           # If this is the last digit
        return digitsMap[digitString[0]]                # Return the corresponding list
    nexts = digitsToLeters(digitString[1:], digitsMap)  # Otherwise, recurse the function forward
    if not nexts:                                       # If any of the later digits return None
        return None                                     # Also return None, error will be flagged above
    holder = []                                         # If all tests are passed, create a return holder
    for letter in digitsMap[digitString[0]]:            # For each letter in the list
        for combination in nexts:                       # Take each combination returned
            holder.append(letter + combination)         # Add the letter to the combination and add it to holder
    return holder                                       # Return the holder


# In[4]:


digitsMap = {
    '2' : ['a', 'b', 'c'],
    '3' : ['d', 'e', 'f'],
    '4' : ['g', 'h', 'i'],
    '5' : ['j', 'k', 'l'],
    '6' : ['m', 'n', 'o'],
    '7' : ['p', 'q', 'r'],
    '8' : ['s', 't', 'u'],
    '9' : ['v', 'w', 'x'],
    '0' : ['y', 'z']
}


# In[30]:


print('The mapping is given below:')
for digit, value in digitsMap.items():
    print('{} : {}'.format(digit, value))


# In[33]:


digits = input('Given a combination of digits:')
print('The combinations are printed below')
print(digitsToLeters(digits, digitsMap))


# In[ ]:




