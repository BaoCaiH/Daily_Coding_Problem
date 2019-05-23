#!/usr/bin/env python
# coding: utf-8
"""2019 May 23rd - Daily_Coding_Problem #128."""
# <markdown>
# ## 2019 May 23rd - Daily_Coding_Problem #128
#
# Problem: The Tower of Hanoi is a puzzle game with three rods and n disks,
# each a different size.
#
# All the disks start off on the first rod in a stack.
#
# They are ordered by size, with the largest disk on the bottom and the
# smallest one at the top.
#
# The goal of this puzzle is to move all the disks from the first rod to
# the last rod while following these rules:
#
# You can only move one disk at a time.
#
# A move consists of taking the uppermost disk from one of the stacks and
# placing it on top of another stack.
#
# You cannot place a larger disk on top of a smaller disk.
#
# Write a function that prints out all the steps necessary to complete the
# Tower of Hanoi. You should assume that the rods are numbered, with the first
# rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod
# being 3.
#
# For example, with n = 3, we can do this in 7 moves:
#
#
# `Move 1 to 3
# Move 1 to 2
# Move 3 to 2
# Move 1 to 3
# Move 2 to 1
# Move 2 to 3
# Move 1 to 3`
#
# My thought process for this problem only stop at 2 pegs and hoped it work out


# %%
def towerOfHanoi(n, source=None, auxiliary=None, goal=None):
    """
    Move the pegs base on the 4 general rules.

    1. No odd disk may be placed directly on an odd disk.

    2. No even disk may be placed directly on an even disk.

    3. There will sometimes be two possible pegs: one will have disks,
    and the other will be empty. Place the disk on the non-empty peg.

    4. Never move a disk twice in succession.
    """
    # Prepare the tower of Hanoi
    if all([not source, not auxiliary, not goal]):
        source = ['source'] + [n-i for i in range(n)]
        auxiliary = ['auxiliary']
        goal = ['goal']
        print('{} | {} | {}'.format(source, auxiliary, goal))

    # If the n is odd/1, the first move is to the goal rod
    if n == 1:
        goal.append(source.pop())
        print('Move {} from {} to {}'.format(goal[-1], source[0], goal[0]))
    else:
        # If n is even, this will make the first move goes to auxiliary
        towerOfHanoi(n-1, source, goal, auxiliary)
        goal.append(source.pop())
        print('Move {} from {} to {}'.format(goal[-1], source[0], goal[0]))
        towerOfHanoi(n-1, auxiliary, source, goal)

    if len(goal) == n+1 and all([len(source) == 1, len(auxiliary) == 1]):
        print('{} | {} | {}'.format(source, auxiliary, goal))


# %%
towerOfHanoi(3)
# %%
towerOfHanoi(4)
