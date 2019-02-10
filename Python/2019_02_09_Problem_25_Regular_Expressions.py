#!/usr/bin/env python
# coding: utf-8

# ## 2019 February 9th
# 
# Problem: Implement regular expression matching with the following special characters:
# 
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
# 
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
# 
# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
# 
# 

# In[47]:


s1 = 'chats'
reg1 = '.*at'
s2 = 'killer'
s3 = 'thriller'
s4 = 'todlers'
reg2 = 't*ler.'
reg3 = 't*ler*'


# In[49]:


def reg_ex(string, reg):
    
    def reg_lst(reg):                                                        # Sub func to turn reg_ex to a list
        lst = []                                                             # So it's easier to process
        txt = ''
        for c in reg:                                                        # For each character
            if c != '.' and c != '*':                                        # Separate them into text vs special
                txt += c                                                     # Texts will be pasted together
            else:                                                            # Special chars, separately
                if txt:
                    lst.append(txt)
                    txt = ''
                lst.append(c)
        if txt:
            lst.append(txt)
        return lst
    
    reg_lst = reg_lst(reg)                                                   # Run the sub-function
    result = []                                                              # A match reg_ex must true at all places, so a list
    ist = 0                                                                  # String index, counter of sort
    iex = 0                                                                  # Reg_ex index
    for i, reg in enumerate(reg_lst):                                        # Iterate through the reg_ex list
        if reg != '.' and reg != '*':                                        # We deal with strings only
            if reg not in string:                                            # If it's not in, immediatly False
                return False
            else:                                                            # Else, check before it
                j = string.index(reg)                                        # If the number of characters before it
                sub_reg_lst = reg_lst[iex:i]                                 # matches the number suggested by reg_ex
                sub_string = string[ist:j]                                   # then give a True component to the list
                if '*' in sub_reg_lst:                                       # The number suggested by reg_ex will be
                    result.append(len(sub_string) >= sub_reg_lst.count('.')) # Affected by the '*' so they will have
                else:                                                        # different sign because '*' allows
                    result.append(len(sub_string) == sub_reg_lst.count('.')) # flexibility
                ist = j + len(reg)                                           # Move the counter so the reg_ex won't be
                iex = i + 1                                                  # counted twice
    if reg_lst[-1] == '.' or reg_lst[-1] == '*':                             # At the end, if there's still reg_ex
        sub_reg_lst = reg_lst[iex:]                                          # repeat the procedure above
        sub_string = string[ist:]
        if '*' in sub_reg_lst:
            result.append(len(sub_string) >= sub_reg_lst.count('.'))
        else:
            result.append(len(sub_string) == sub_reg_lst.count('.'))
    else:                                                                    # If not, check if the string has ended
        if len(string) > ist:
            return False
                    
    
    return all(result)                                                       # If all the elements are True


# In[43]:


print('Given the string: "{}" and the regular expression "{}", the matching results would be {}'.format(s1, reg1, reg_ex(s1, reg1)))
print('Given the same string without "s": "{}" and the regular expression "{}", the matching results would be {}'.format(s1[0:4], reg1, reg_ex(s1[0:4], reg1)))


# In[45]:


print('Given the strings: "{}", "{}" and "{}", and the regular expression "{}"'.format(s2, s3, s4, reg2))
print('The matching results will be as follow: {}, {}, and {}'.format(reg_ex(s2, reg2), reg_ex(s3, reg2), reg_ex(s4, reg2)))


# In[48]:


print('But if we change the regular expression to "{}", the matching results will be as follow: {}, {} and {}'.format(
reg3, reg_ex(s2, reg3), reg_ex(s3, reg3), reg_ex(s4, reg3)))

