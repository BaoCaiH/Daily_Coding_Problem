#!/usr/bin/env python
# coding: utf-8
"""2019 June 27th - Daily_Coding_Problem #163."""
# <markdown>
# ## 2019 June 27th - Daily_Coding_Problem #163
#
# This problem was asked by Jane Street.
#
# Given an arithmetic expression in Reverse Polish Notation,
# write a program to evaluate it.
#
# The expression is given as a list of numbers and operands.
# For example: [5, 3, '+'] should return 5 + 3 = 8.
#
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
# should return 5, since it is equivalent to
# ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
#
# You can assume the given expression is always valid.


# %%
def calculator(nums, operators):
    """Calculate the result given the numbers and operators."""
    result = nums[0]
    nums.pop(0)
    for i in range(len(operators)):
        if operators[i] == '+':
            result = nums[i] + result
        elif operators[i] == '-':
            result = nums[i] - result
        elif operators[i] == '*':
            result = nums[i] * result
        elif operators[i] == '/':
            result = nums[i] / result
        elif operators[i] == '**':
            result = nums[i] ** result
        elif operators[i] == '//':
            result = nums[i] // result
        elif operators[i] == '%':
            result = nums[i] % result
    return result


# %%
def reversePolishNotation(opr):
    """Evaluate an arithmetic expression in Reverse Polish Notation."""
    nums = []
    operators = []
    prevType = None
    currType = None
    for e in opr:
        if not prevType:
            prevType = type(e)
            nums = [e] + nums
        else:
            currType = type(e)
            if currType == prevType:
                if isinstance(e, str):
                    operators.append(e)
                else:
                    nums = [e] + nums
            else:
                if isinstance(e, str):
                    operators.append(e)
                    prevType = currType
                else:
                    nums = [e, calculator(nums, operators)]
                    operators = []
                    prevType = currType
    return calculator(nums, operators)


# %%
operations = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
# %%
reversePolishNotation(operations)
