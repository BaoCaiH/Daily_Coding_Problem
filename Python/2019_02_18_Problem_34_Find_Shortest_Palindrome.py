#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 18th
# 
# Problem: Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
# 
# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# 
# As another example, given the string "google", you should return "elgoogle".
# 
# ***I did not come up with the solution for this problem. The original solution can be found [here](https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_31_35.py)***
# 
# ***All I did was de-loaded certain steps and added explanations, for me and anyone who want to read***

# In[12]:


def find_palindrome(string): 
    
    # Sub-function to find possibilities
    def palindromes(string, front, back):
        if not front or not back:  # If either side is missing
            return front +\        # Paste the available side
                    back[::-1] +\  # backward
                    string +\      # with the already establish palindrome in the middle
                    front[::-1] +                    back
        
        if front[-1] == back[0]:                             # If the 2 chars one 2 sides are the same
            return palindromes(front[-1] + string + back[0], # paste it, and re-apply the function
                              front[:-1],                    # Remove the used characters
                              back[1:])                      # on both sides
        
        use_front_char = palindromes(front[-1] + string + front[-1], # If the 2 chars are different
                                    front[:-1],                      # Use 2 cases,
                                    back)                            # paste the front char around
        use_back_char = palindromes(back[0] + string + back[0],      # and move on
                                   front,                            # Then paste the back and move on
                                   back[1:])
        
        if len(use_front_char) == len(use_back_char): # If the 2 cases are equally short
            return min(use_front_char, use_back_char) # Then use the string that is lexicographically smaller
        else:                                         # Else, choose the shorter one
            return [use_front_char, use_back_char][len(use_front_char) > len(use_back_char)]
        
    possible_palindromes = []
    # It will loop through the string
    # Treat each one as a possible center
    # And run the sub-function
    # Including the space between 2 characters
    for i in range(len(string)):
        possible_palindromes.append(palindromes(string[i],     # Center character
                                                string[:i],    # everything before the center
                                                string[i+1:])) # everything after
        possible_palindromes.append(palindromes('',            # Center space
                                               string[:i],     # everything before the space
                                               string[i:]))    # everything after
    # Find the min length
    min_palindrome_length = min(map(len, possible_palindromes))
    # Then filter to keep only the shortest ones
    possible_palindromes = filter(lambda palindrome: len(palindrome) == min_palindrome_length,
                                  possible_palindromes)
    
    return min(possible_palindromes) # Choose the string that is lexicographically smaller


# In[15]:


s1 = 'race'
s2 = 'book'
s3 = 'google'
s4 = 'elamaan'


# In[18]:


print('This solution was not founded by me, please refer to the original solution in the description, the hyperlink, if needed')
print('For solution explanation, refer to the function, there are explanations in comments')
print('Given 4 strings \'{}\', \'{}\', \'{}\' and \'{}\''.format(s1, s2, s3, s4))
print('The shortest strings in length and lexicographically are \'{}\', \'{}\', \'{}\' and \'{}\''.format(
find_palindrome(s1), find_palindrome(s2), find_palindrome(s3), find_palindrome(s4)))

