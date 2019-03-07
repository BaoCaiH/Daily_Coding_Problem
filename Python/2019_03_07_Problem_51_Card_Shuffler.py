#!/usr/bin/env python
# coding: utf-8

# ## 2019 March 7th
# 
# Problem: Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
# 
# It should run in O(N) time.
# 
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

# In[11]:


# This function explanation can be found at the solution for question #15
def random_number(n):
    import random
    number = None
    for i in range(n):
        if i == 0:
            number = i
        elif random.randint(0, i) == 0:
            number = i
    return number


# In[18]:


# Since the function above generates a random number in the range of a deck of card
# We just simply need to swap
def shuffle_deck(cards, n):
    for i, e in enumerate(cards):
        swap_with = random_number(n)
        cards[i], cards[swap_with] = cards[swap_with], cards[i]


# In[19]:


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
       14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
       40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]


# In[20]:


i = 0
for _ in range(4):
    print(deck[i:i+13])
    i += 13


# In[21]:


shuffle_deck(deck, 52)
i = 0
for _ in range(4):
    print(deck[i:i+13])
    i += 13

