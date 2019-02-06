#!/usr/bin/env python
# coding: utf-8

# ## 2019 January 22nd
# 
# Problem: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# 
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# 
# You can assume that the messages are decodable. For example, '001' is not allowed.

# In[46]:


def decoding(string):
    if len(string) <= 1:                                        # If the string is only 1 digit long then there would only be 1 result, including empty string
        return 1                                                # because toward the end, we need to count 1 to account for the instance happen before it
    elif int(string[0]) == 0 or '00' in string:                 # Also because 0 does not have any assigned value so it cannot be decoded if they stand together or at the beginning of the string
        return print('Not decodable')
    else:                                                       # Otherwise, let's check inside the string
        if int(string[0:2]) == 10 or int(string[0:2]) == 20:    # 2 special cases are 10 and 20, they only have 1 way to decode them, so we jump 2 digits
            return decoding(string[2:])                         # Cut the 2 digits from the string and continue to decode the rest of the string
        elif int(string[0:2]) <= 26:                            # If they are anything less than 26, they have 2 ways to decode
            return decoding(string[1:]) + decoding(string[2:])  # So cut them 2 different ways
        else:                                                   # If they are larger than 26
            return decoding(string[1:])                         # There is also only one way to decode that is individually


# In[48]:


print('Give a random string:')
string = input()
decoding(string)

