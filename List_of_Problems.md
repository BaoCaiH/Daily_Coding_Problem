# Daily Coding Problem

Own solutions, a few of them are learnt from other programmer online.

## Problem 1

This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_16_Problem_1_of_check_sum.py)

## Problem 2

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_17_Problem_2_Products_of_other_elements_in_list.py)

## Problem 3

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_18_Problem_3_Serialize_and_De-serialize_a_Binary_Tree.py)

## Problem 4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_19_Problem_4_Smallest_missing_integer.py)

## Problem 5

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_20_Problem_5_Construct_and_Deconstruct_a_pair.py)

## Problem 7

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example,
'001' is not allowed.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_22_Problem_7_Decode_a_number_string.py)

## Problem 8

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:


`>   0
  / \
 1   0
    / \
   1   0
  / \
 1   1`

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_23_Problem_8_Unival_Trees.py)
