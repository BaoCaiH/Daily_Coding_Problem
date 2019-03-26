#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 26th
# 
# Problem: A number is considered perfect if its digits sum up to exactly 10.
# 
# Given a positive integer n, return the n-th perfect number.
# 
# For example, given 1, you should return 19. Given 2, you should return 28.

# In[9]:


def is_perfect_number(number):              # Supporting function
    total = 0                               # Sum of all the digits
    while number > 0:                       #
        total += number % 10                # Take each digit by retrieve the remainder when divide by 10
        number = number // 10               # Then remove that digit
    return True if total == 10 else False   # 
                                            #
def n_th_perfect_number(n):                 #
    counter = 0                             # Count the n-th number
    integer = 19                            # The smallest perfect number is 19 so start here
    while True:                             # This loop will only stop when it finds a number fits requirement
        if is_perfect_number(integer):      # If the integer is perfect (by this question definition, not math)
            counter += 1                    # Increase the counter
            if counter == n:                # Check if the n-th is met
                return integer              # Then return the integer
        integer += 1                        # If not, increase the integer by 1 and continue


# In[11]:


n = int(input('Which perfect number do you want to see (i.e: 5th)?: '))
n_th_perfect_number(n)

