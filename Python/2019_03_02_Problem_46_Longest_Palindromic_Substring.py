#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 2nd
# 
# Problem: Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
# 
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

# In[49]:


def longest_palindromic_subs(string):
    
    # Sub function to return any possible palindrome from a position in the original string
    # It will be feed with a character or a position in the original string
    # If the either side is used up, just return the given substring
    # If the next character on both sides are equal to each other,
    # add it to the substring and recurse the function until it is used up
    # Or the two sides are no longer similar then also return the substring
    def palindromes(sub, front, back):    
        if not front or not back:
            return sub
        
        if front[-1] == back[0]:
            return palindromes(front[-1] + sub + back[0],
                               front[:-1], back[1:])
        else:
            return sub
    
    # In the main function
    # We need a holder
    # Then at each position in the string, run the sub-function twice
    # First with the character at the position as the center
    # Then with the gap between this character and the previous as the center
    # All those will appear in the possible holder
    possible_palindromes = []
    for i in range(len(string)):
        possible_palindromes.append(palindromes(string[i],
                                                string[:i],
                                                string[i+1:]))
        possible_palindromes.append(palindromes('',
                                                string[:i],
                                                string[i:]))
    
    # Filter the holder from any None or '' results
    possible_palindromes = [palindrome for palindrome in possible_palindromes if palindrome]
    
    # Find out the max length in the holder
    max_length = max(map(len, possible_palindromes))
    
    # Filter again
    possible_palindromes = filter(lambda palindrome: len(palindrome) == max_length, possible_palindromes)
    
    # Return the lexicographically largest, because why not
    return max(possible_palindromes)


# In[2]:


s1 = 'aabcdcb'
s2 = 'bananas'


# In[48]:


print('Given the two strings \'{}\' and \'{}\''.format(s1, s2))
print('The longest palindromic substrings are \'{}\' and \'{}\' respectively'.format(longest_palindromic_subs(s1), longest_palindromic_subs(s2)))

