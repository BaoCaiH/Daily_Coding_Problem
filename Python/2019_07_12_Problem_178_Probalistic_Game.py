#!/usr/bin/env python
# coding: utf-8
"""2019 July 12th - Daily_Coding_Problem #178."""
# <markdown>
# ## 2019 July 12th - Daily_Coding_Problem #178
#
# This problem was asked by Two Sigma.
#
# Alice wants to join her school's Probability Student Club.
# Membership dues are computed via one of two simple probabilistic games.
#
# The first game: roll a die repeatedly. Stop rolling once you get a five
# followed by a six. Your number of rolls is the amount you pay, in dollars.
#
# The second game: same, except that
# the stopping condition is a five followed by a five.
#
# Which of the two games should Alice elect to play? Does it even matter?
# Write a program to simulate the two games and calculate their expected value.


# %%
def diceGame(first, second, prev=0, rolls=0):
    """Play the dice game given the first and second win conditions."""
    from random import randint
    rand = randint(1, 6)
    rolls += 1
    if prev == first and rand == second:
        return rolls
    return diceGame(first, second, rand, rolls)


# %%
def expectedRolls(firstCondition, secondCondition, k=10000):
    """Simulate to dice game k times."""
    total = 0
    for _ in range(k):
        total += diceGame(firstCondition, secondCondition)
    return total/k


# %%
print(expectedRolls(5, 5))
print(expectedRolls(5, 6))
