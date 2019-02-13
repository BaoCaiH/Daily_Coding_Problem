#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 12th
# 
# Problem: Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
# 
# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
# 
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# 
# Each word is guaranteed not to be longer than k.
# 
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# 
# `["the  quick brown",` # 1 extra space on the left<br>
# `"fox  jumps  over",` # 2 extra spaces distributed evenly<br>
# `"the   lazy   dog"]` # 4 extra spaces distributed evenly

# In[54]:


def justify_text(lst, k):
    def paste_text(lst, k):                                 # Sub-func to help paste the strings
        if len(lst) == 1:                                   # If the list only has 1 element
            n_space_left = k - len(lst[0])                  # FInd out how many spaces are needed
            return lst[0] +  ' ' * n_space_left             # Then paste it at the end
        n_required_space = lst.count(' ')                   # Count the number of spaces needed
        n_space_left = k - len(''.join(lst))                # And how many more to fill in
        while n_space_left > 0:                             # Until there is no spaces left
            for i, e in enumerate(lst):                     # Loop through the text list
                if ' ' in e:                                # If it's a space element
                    lst[i] = e + ' '                        # Add 1 more space
                    n_space_left -= 1                       # Reduce 1 space from the pool
                    if n_space_left == 0:                   # If it's empty
                        return ''.join(lst)                 # Return the joined string
    # Main function starts here
    temp_lst = []                                           # Create a holder for strings
    results = []                                            # And the results list
    for e in lst:                                           # For each element of the list
        if not temp_lst:                                    # If the holder is empty
            temp_lst.append(e)                              # Just put the element in as the start of the string
        else:                                               # Otherwise
            text_length = len(''.join(temp_lst))            # Find out the length at that point
            e_length = len(e)                               # Also the length of the new element
            if text_length + e_length + 1 == k:             # If their sum fits just fine with the required k
                results.append(''.join(temp_lst) + ' ' + e) # Paste them together and add to the results list
                temp_lst = []                               # Empty the holder
            elif text_length + e_length + 1 > k:            # If the length is larger:
                results.append(paste_text(temp_lst, k))     # Paste what ever is in the temp list
                temp_lst = [e]                              # Then replace the temp list with a new list
            elif text_length + e_length + 1 < k:            # If the length is smaller
                temp_lst.append(' ')                        # Add a space
                temp_lst.append(e)                          # And add the element
    if temp_lst:                                            # If the temp list still has some element
        results.append(paste_text(temp_lst, k))             # Paste them already
    return results                                          # Here are the results


# In[52]:


l = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 17
sl = ["Don't", 'learn', 'to', 'code', 'blindly', 'like', 'reading', 'a', 'text', 'book', 'Learn', 'to', 'solve', 'problems']
sk = 16


# In[42]:


print('Given the list {} and k is {}'.format(l, k))
print('The justified text looks like this: {}'.format(justify_text(l, k)))


# In[55]:


print('Given the list {} and k is {}'.format(sl, sk))
print('The justified text looks like this: {}'.format(justify_text(sl, sk)))

