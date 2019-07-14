#!/usr/bin/env python
# coding: utf-8
"""2019 July 9th - Daily_Coding_Problem #175."""
# <markdown>
# ## 2019 July 9th - Daily_Coding_Problem #175
#
# This problem was asked by Google.
#
# You are given a starting state start, a list of transition probabilities
# for a Markov chain, and a number of steps num_steps.
# Run the Markov chain starting from start for num_steps and
# compute the number of times we visited each state.
#
# For example, given the starting state `a`, number of steps `5000`,
# and the following transition probabilities:
#
# `[
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]`
#
# One instance of running this Markov chain might produce
# `{ 'a': 3012, 'b': 1656, 'c': 332 }`.


# %%
def markowChain(state, steps, possibilities):
    """Return an instance of the Markov chain."""
    from random import random
    transition = {}
    production = {}
    for p in possibilities:
        if p[0] not in transition:
            transition[p[0]] = {p[1]: p[2]}
            production[p[0]] = 0
        else:
            transition[p[0]][p[1]] = list(transition[p[0]].values())[-1]+p[2]
    for _ in range(steps):
        prob = random()
        for dest, p in transition[state].items():
            if prob <= p:
                production[state] += 1
                state = dest
                break
    return production


# %%
examplePossibilities = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
exampleState = 'a'
exampleSteps = 5000
markowChain(exampleState, exampleSteps, examplePossibilities)
