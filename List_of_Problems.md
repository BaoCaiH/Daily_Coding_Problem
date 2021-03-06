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

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_23_Problem_8_Unival_Trees.py)

## Problem 9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_24_Problem_9_Largest_Sum_of_Non-adjacent_Numbers.py)

## Problem 10

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_25_Problem_10_Job_Scheduler.py)

## Problem 11

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a
set of all possible query strings, return all strings in the set that have s
as a prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_26_Problem_11_Auto-correct.py)

## Problem 12

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2
steps at a time. Given N, write a function that returns the number of unique
ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

```
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
```

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_27_Problem_12_Stepping_ways.py)

## Problem 13

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_28_Problem_13_Longest_Substring_with_nDistinct_Characters.py)

## Problem 14

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places
using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_29_Problem_14_Pi_Calculator.py)

## Problem 15

This problem was asked by Facebook.

Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_30_Problem_15_Random_Picker.py)

## Problem 16

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

```
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
```

You should be as efficient with time and space as possible.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_01_31_Problem_16_Database_and_API.py)

## Problem 17

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

```
dir
    subdir1
    subdir2
        file.ext
```

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2 \n\t\t\tfile2.ext" represents:

```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_01_Problem_17_Longest_Absolute_Path.py)

## Problem 18

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

```
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
```

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_02_Problem_18_Max_Value_from_Sub-array_Length_k.py)

## Problem 19

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_03_Problem_19_n_k_Cost_Matrix.py)

## Problem 20

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_04_Problem_20_Intersect_Node.py)

## Problem 21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_05_Problem_21_Minimum_Classrooms.py)

## Problem 22

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_06_Problem_22_Return_Sentence.py)

## Problem 23

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

```
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
```

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_07_Problem_23_Minimum_Steps.py)

## Problem 24

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

```
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
```

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

Solution

## Problem 25

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

```
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
```

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".\*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_09_Problem_25_Regular_Expressions.py)

## Problem 26

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_09_Problem_26_Remove_kth_last.py)

## Problem 27

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "`([])[]({})`", you should return true.

Given the string "`([)]`" or "`((()`", you should return false.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_11_Problem_27_Balance_Brackets.py)

## Problem 28

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_12_Problem_28_Justify_Text.py)

## Problem 29

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_13_Problem_29_Run-length_Encode.py)

## Problem 30

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_14_Problem_30_Water_Holding.py)

## Problem 31

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_15_Problem_31_Edit_Distance.py)

## Problem 32

This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

Solution

# Problem 33

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

```
2
1.5
2
3.5
2
2
2
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_17_Problem_33_Print_Median.py)

## Problem 34

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_18_Problem_34_Find_Shortest_Palindrome.py)

## Problem 35

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_19_Problem_35_RGB_Swapping.py)

## Problem 36

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_20_Problem_36_Second_Largest_Node.py)

## Problem 37

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_21_Problem_37_Power_Set.py)

## Problem 38

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_22_Problem_38_N_Queen.py)

## Problem 39

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

```
Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
```

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (\*) and a dead cell with a dot (.).

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_23_Problem_39_Conway_Game.py)

## Problem 40

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_24_Problem_40_Non_Triplet.py)

## Problem 41

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_25_Problem_41_Flight_Itinerary_in_Lexicography.py)

## Problem 42

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_26_Problem_42_Target_Sum_Subset.py)

## Problem 43

This problem was asked by Amazon.

Implement a stack that has the following methods:

```
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
```

Each method should run in constant time.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_27_Problem_43_Stack_Object.py)

## Problem 44

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_02_28_Problem_44_Inversions.py)

## Problem 45

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_01_Problem_45_Random_7_Uniformly_by_Random_5_Uniformly.py)

## Problem 46

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_02_Problem_46_Longest_Palindromic_Substring.py)

## Problem 47

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_03_Problem_47_Max_Profit.py)

## Problem 48

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

```
    a
   / \
  b   c
 / \ / \
d  e f  g
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_04_Problem_48_Reconstruct_Tree_from_Preorder_and_Inorder.py)

## Problem 49

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_05_Problem_49_Max_Sum_of_Contiguous_Subsets.py)

## Problem 50

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return 45, as it is (3 + 2) * (4 + 5).

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_06_Problem_50_Arithmetic_Tree.py)

## Problem 51

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_07_Problem_51_Card_Shuffler.py)

## Problem 52

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

```
set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
```

Each operation should run in O(1) time.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_08_Problem_52_LRU_Cache.py)

## Problem 53

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_09_Problem_53_Queue_by_Two_Stacks.py)

## Problem 54

This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_10_Problem_54_Sudoku_Solver.py)

## Problem 55

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

```
shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
```

Hint: What if we enter the same URL twice?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_11_Problem_55_URL_Shortener.py)

## Problem 56

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_12_Problem_56_Coloring_Vertex_in_Adjacency_Matrix.py)

## Problem 57

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_13_Problem_57_String_Breaker.py)

## Problem 58

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_14_Problem_58_Indexing.py)

## Problem 59

This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

Solution

## Problem 60

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_16_Problem_60_Split_Set.py)

## Problem 61

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_17_Problem_61_Integer_Exponential.py)

## Problem 62

This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_18_Problem_62_Matrix_Crossing.py)

## Problem 63

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

```
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
```

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_19_Problem_63_WORDSSSSS.py)

## Problem 64

This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_20_Problem_64_%20Knight_Tours.py)

## Problem 65

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

```
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```

You should print out the following:

```
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_21_Problem_65_%20Clockwise_Print.py)

## Problem 66

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_22_Problem_66_Unbias_the_Biased.py)

## Problem 67

This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

```
set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
```

Each operation should run in O(1) time.

Solution

## Problem 68

This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

```
(0, 0)
(1, 2)
(2, 2)
(4, 0)
```

The board would look like this:

```
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
```

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_24_Problem_68_Bishop_Attacking_Pairs.py)

## Problem 69

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_25_Problem_69_Largest_Product_of_Three.py)

## Problem 70

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_26_Problem_70_n_th_Perfect_Number.py)

## Problem 71

This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

Solution

## Problem 72

This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

```
ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
```

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

```
A

[(0, 0)]
```

Should return null, since we have an infinite loop.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_28_Problem_72_Largest_Value_Path.py)

## Problem 73

This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_29_Problem_73_Reverse_Singly_Linked_List.py)

## Problem 74

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

```
| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |
```

And there are 4 12's in the table.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_30_Problem_74_Multiplication_Table.py)

## Problem 75

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_03_31_Problem_75_Longest_Increasing_Subsequence.py)

## Problem 76

This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

```
cba
daf
ghi
```

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

```
ca
df
gi
```

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

```
abcdef
```

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

```
zyx
wvu
tsr
```

Your function should return 3, since we would need to remove all the columns to order it.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_01_Problem_76_Columns_To_Remove.py)

## Problem 77

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_02_Problem_77_Overlapping_Intervals.py)

## Problem 78

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_03_Problem_78_Merge_k_Singly_Linked_List.py)

## Problem 79

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_04_Problem_79_Non_Decreasing_Array.py)

## Problem 80

This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

```
    a
   / \
  b   c
 /
d
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_05_Problem_80_Deepest_Node.py)

## Problem 81

This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_06_Problem_81_Digits_to_Letters.py)

## Problem 82

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_07_Problem_82_readN_from_read7.py)

## Problem 83

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

```
    a
   / \
  b   c
 / \  /
d   e f
```

should become:

```
  a
 / \
 c  b
 \  / \
  f e  d
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_08_Problem_83_Invert_Binary_Tree.py)

## Problem 84

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

```
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_09_Problem_84_Find_Islands.py)

## Problem 85

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_10_Problem_85_X_Or_Y.py)

## Problem 86

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_11_Problem_86_Remove_Parantheses.py)

## Problem 87

This problem was asked by Uber.

A rule looks like this:

```
A NE B
```

This means this means point A is located northeast of point B.

```
A SW C
```

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

```
A N B
B NE C
C N A
```

does not validate, since A cannot be both north and south of C.

```
A NW B
A N B
```

is considered valid.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_12_Problem_87_Direction_Rules.py)

## Problem 88

This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_13_Problem_88_Divide_without_Dividing.py)

## Problem 89

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_14_Problem_89_Binary_Search_Tree.py)

## Problem 90

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_15_Problem_90_Random_Integer_Not_In_List.py)

## Problem 91

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```
functions = []
for i in range(10):
    functions.append(lambda : i)
```
```
for f in functions:
    print(f())
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_16_Problem_91_Fixing_Lambda.py)

## Problem 92

This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_17_Problem_92_Study_Track.py)

## Problem 93

This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_18_Problem_93_Largest_Binary_Search_Tree.py)

## Problem 94

This problem was asked by Google.

Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_19_Problem_94_Max_Path_Sum.py)

## Problem 95

This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_20_Problem_95_Next_Greater_Permutation.py)

## Problem 96

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_21_Problem_96_All_Permutation.py)

## Problem 97

This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

```
set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.
```

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

```
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_22_Problem_97_Key_Time_Value.py)

## Problem 98

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_23_Problem_98_Find_Words.py)

## Problem 99

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_24_Problem_99_Longest_Consecutive_Sequence.py)

## Problem 100

This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

```
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_25_Problem_100_Minimum_Steps.py)

## Problem 101

This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_26_Problem_101_Goldbach_Pair.py)

## Problem 102

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_25_Problem_102_Contiguous_Sum.py)

## Problem 103

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_28_Problem_103_Shortest_Substring.py)

## Problem 104

This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_29_Problem_104_Palindrome_Linked_List.py)

## Problem 105

This problem was asked by Facebook.

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_04_30_Problem_105_Debounce.py)

## Problem 106

This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_01_Problem_106_Hopping.py)

## Problem 107

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

```
  1
 / \
2   3
   / \
  4   5
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_02_Problem_107_Print_Binary_Tree_Level_Wise.py)

## Problem 108

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_03_Problem_108_Shifting_Strings.py)

## Problem 109

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_04_Problem_109_Swap_Bits.py)

## Problem 110

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

```
   1
  / \
 2   3
    / \
   4   5
```

Return [[1, 2], [1, 3, 4], [1, 3, 5]].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_05_Problem_110_Root_to_Leaves.py)

## Problem 111

This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_06_Problem_111_Anagrams.py)

## Problem 112

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_07_Problem_112_Lowest_Common_Ancestor.py)

## Problem 113

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_08_Problem_113_Reverse_String.py)

## Problem 114

This problem was asked by Facebook.

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_09_Problem_114_Reverse_String_With_Any_Delimiter.py)

## Problem 115

This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_10_Problem_115_Child_Branch.py)

## Problem 116

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_11_Problem_116_Generate_Arbitrary_Large_Tree.py)

## Problem 117

This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_12_Problem_117_Binary_Tree_Minimum_Level.py)

## Problem 118

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_13_Problem_118_Square_And_Sort.py)

## Problem 119

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_14_Problem_119_Smallest_Set.py)

## Problem 120

This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of `getInstance()`, return the first instance and in every odd call of `getInstance()`, return the second instance.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_15_Problem_120_Twisted_Singleton.py)

## Problem 121

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_16_Problem_121_Make_Palindrome_by_Removing_k_Char.py)

## Problem 122

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at `matrix[0][0]`, and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

```
0 3 1 1
2 0 0 4
1 5 3 1
```

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_17_Problem_122_Collect_Max_Coins.py)

## Problem 123

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

```
"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
```

And here are examples of non-numbers:

```
"a"
"x 1"
"a -2"
"-"
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_18_Problem_123_Is_Number.py)

## Problem 124

This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_19_Problem_124_Flip_k_Coins.py)

## Problem 125

This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

```
    10
   /   \
 5      15
       /  \
     11    15
```

Return the nodes 5 and 15.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_20_Problem_125_Sum_Node_Pair_to_k.py)

## Problem 126

This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, `[1, 2, 3, 4, 5, 6]` rotated by two becomes `[3, 4, 5, 6, 1, 2]`. Try solving this without creating a copy of the list. How many swap or move operations do you need?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_21_Problem_126_Rotate_List.py)

## Problem 127

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

```
1 -> 2 -> 3 -> 4 -> 5
```

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

```
9 -> 9
5 -> 2
```

return 124 (99 + 25) as:

```
4 -> 2 -> 1
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_22_Problem_127_Linked_List_As_Int.py)

## Problem 128

The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.

A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.

You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

```
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_23_Problem_128_Tower_of_Hanoi.py)

## Problem 129

Given a real number n, find the square root of n. For example, given n = 9, return 3.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_24_Problem_129_Square_Root.py)

## Problem 130

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_25_Problem_130_Stock_Market.py)

## Problem 131

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_26_Problem_131_Random_List.py)

## Problem 132

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

```
record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
```

Follow-up: What if our system has limited memory?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_27_Problem_132_Hit_Counter.py)

## Problem 133

This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

```
   10
  /  \
 5    30
     /  \
   22    35
```

You can assume each node has a parent pointer.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_28_Problem_133_Inorder_Successor.py)

## Problem 134

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

```
init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_29_Problem_134_Sparse_Array.py)

## Problem 135

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_30_Problem_135_Minimum_Path.py)

## Problem 136

This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

```
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
```

Return 4.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_05_31_Problem_136_Largest_Rectangle.py)

## Problem 137

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

```
init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_01_Problem_137_Bit_Array.py)

## Problem 138

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_02_Problem_138_n_Cents.py)

## Problem 139

This problem was asked by Google.

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

```
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```
[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_03_Problem_139_Peakable_Iterator.py)

## Problem 140

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_04_Problem_140_Get_Single_Elements.py)

## Problem 141

This problem was asked by Microsoft.

Implement 3 stacks using a single list:

```
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_05_Problem_141_Three_Stacks.py)

## Problem 142

This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_06_Problem_142_Balance_String.py)

## Problem 143

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x

The second part contains all elements in lst that are equal to x

The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given `x = 10` and `lst = [9, 12, 3, 5, 14, 10, 10]`, one partition may be `[9, 3, 5, 10, 10, 12, 14]`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_07_Problem_143_Partitioning.py)

## Problem 144

This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_08_Problem_144_Nearest_Larger.py)

## Problem 145

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given `1 -> 2 -> 3 -> 4`, return `2 -> 1 -> 4 -> 3`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_09_Problem_145_Swap_Every_2_Nodes.py)

## Problem 146

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
```

should be pruned to:

```
   0
  / \
 1   0
    /
   1
```

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_10_Problem_146_Prune_Binary_Tree.py)

## Problem 147

Given a list, sort it using this method: `reverse(lst, i, j)`, which reverses lst from i to j.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_11_Problem_147_Sort_by_Reverse.py)

## Problem 148

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for `n = 2`, one gray code would be `[00, 01, 11, 10]`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_12_Problem_148_Gray_Code.py)

## Problem 149

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method `sum(i, j)` which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given `L = [1, 2, 3, 4, 5]`, `sum(1, 3)` should return `sum([2, 3])`, which is 5.

You can assume that you can do some pre-processing. `sum()` should be optimized over the pre-processing step.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_13_Problem_149_Optimized_Sum.py)

## Problem 150

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points `[(0, 0), (5, 4), (3, 1)]`, the central point `(1, 2)`, and `k = 2`, return `[(0, 0), (3, 1)]`.


[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_14_Problem_150_Nearest_k_Points.py)

## Problem 151

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

```
B B W
W W W
W W W
B B B
```

Becomes

```
B B G
G G G
G G G
B B B
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_15_Problem_151_Fill_Color.py)

## Problem 152

This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_16_Problem_152_Generate_From_Histogram.py)

## Problem 153

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_17_Problem_153_Smallest_Distance_Between_2_Words.py)

## Problem 154

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

`push(item)`, which adds an element to the stack
`pop()`, which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

```
push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_18_Problem_154_Heap_Stack.py)

## Problem 155

This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (`> floor(len(lst) / 2.0)`).

You can assume that such element exists.

For example, given `[1, 2, 1, 1, 3, 4, 0]`, return `1`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_19_Problem_155_Majority_Element.py)

## Problem 156

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given `n` = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given `n` = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_20_Problem_156_Smallest_Number_of_Squared.py)

## Problem 157

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, `carrace` should return true, since it can be rearranged to form `racecar`, which is a palindrome. `daily` should return false, since there's no rearrangement that can form a palindrome.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_21_Problem_157_Palindrome_Permutation.py)

## Problem 158

This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

```
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
```

Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right

The top left corner and bottom right corner will always be 0.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_22_Problem_158_Ways_Through_Matrix.py)

## Problem 159

This problem was asked by Google.

Given a string, return the first recurring character in it, or `null` if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return `null`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_23_Problem_159_First_Recurring_Character.py)

## Problem 160

This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

```
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
```

and the weights: `a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1`, the longest path would be `c -> a -> d -> f`, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_24_Problem_160_Random_Tree_Longest_Path.py)

## Problem 161

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number `1111 0000 1111 0000 1111 0000 1111 0000`, return `0000 1111 0000 1111 0000 1111 0000 1111`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_25_Problem_161_Reverse_Bits.py)

## Problem 162

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

```
dog
cat
apple
apricot
fish
```

Return the list:

```
d
c
app
apr
f
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_26_Problem_162_Unique_Prefix.py)

## Problem 163

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: `[5, 3, '+']` should return `5 + 3 = 8`.

For example, `[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']` should return 5, since it is equivalent to `((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5`.

You can assume the given expression is always valid.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_27_Problem_163_Reverse_Polish_Notation.py)

## Problem 164

This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set `{1, 2, ..., n}`. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_28_Problem_164_Pigeonhole.py)

## Problem 165

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array `[3, 4, 9, 6, 1]`, return `[1, 1, 2, 1, 0]`, since:

```
There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_29_Problem_165_Smaller_Elements.py)

## Problem 166

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

`next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.

`has_next()`: returns whether or not the iterator still has elements left.
For example, given the input `[[1, 2], [3], [], [4, 5, 6]]`, calling `next()` repeatedly should output `1, 2, 3, 4, 5, 6`.

Do not use `flatten` or otherwise clone the arrays. Some of the arrays can be empty.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_06_30_Problem_166_2D_Iterator.py)

## Problem 167

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list `["code", "edoc", "da", "d"]`, return `[(0, 1), (1, 0), (2, 3)]`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_01_Problem_167_Palindrome_Pairs.py)

## Problem 168

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

you should return:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

Follow-up: What if you couldn't use any extra space?

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_02_Problem_168_Rotate_Matrix.py)

## Problem 169

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list `4 -> 1 -> -3 -> 99` should become `-3 -> 1 -> 4 -> 99`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_03_Problem_169_Sort_Linked_List.py)

## Problem 170

This problem was asked by Facebook.

Given a `start` word, an end word, and a dictionary of valid words, find the shortest transformation sequence from `start` to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return `null`. Each word in the dictionary have the same length as `start` and `end` and is lowercase.

For example, given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "dop", "dat", "cat"}`, return `["dog", "dot", "dat", "cat"]`.

Given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "tod", "dat", "dar"}`, return `null` as there is no possible transformation from `dog` to `cat`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_04_Problem_170_Transform_Words.py)

## Problem 171

This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

`{"timestamp": 1526579928, count: 3, "type": "enter"}`

This means 3 people entered the building. An exit looks like this:

`{"timestamp": 1526580382, count: 2, "type": "exit"}`

This means that 2 people exited the building. `timestamp` is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of `(start, end)` timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_05_Problem_171_Busiest_Time.py)

## Problem 172

This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given `s = "dogcatcatcodecatdog"` and `words = ["cat", "dog"]`, return `[0, 13]`, since `"dogcat"` starts at index `0` and `"catdog"` starts at index `13`.

Given `s = "barfoobazbitbyte"` and `words = ["dog", "cat"]`, return `[]` since there are no substrings composed of `"dog"` and `"cat"` in `s`.

The order of the indices does not matter.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_06_Problem_172_Starting_Indices.py)

## Problem 173

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

```
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
```

it should become:

```
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```

You can assume keys do not contain dots in them, i.e. no clobbering will occur.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_07_Problem_173_Flatten_Nested_Dictionary.py)

## Problem 174

This problem was asked by Google.

You are given a starting state `start`, a list of transition probabilities for a Markov chain, and a number of steps `num_steps`. Run the Markov chain starting from `start` for `num_steps` and compute the number of times we visited each state.

For example, given the starting state `a`, number of steps 5000, and the following transition probabilities:

```
[
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
```

One instance of running this Markov chain might produce `{ 'a': 3012, 'b': 1656, 'c': 332 }`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_09_Problem_175_Markov_Chain.py)

## Problem 176

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string `s1` to another `s2`.

For example, given `s1 = abc` and `s2 = bcd`, return `true` since we can map `a` to `b`, `b` to `c`, and `c` to `d`.

Given `s1 = foo` and `s2 = bar`, return `false` since the `o` cannot map to two characters.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_10_Problem_176_Character_Mapping.py)

## Problem 177

This problem was asked by Airbnb.

Given a linked list and a positive integer `k`, rotate the list to the right by `k` places.

For example, given the linked list `7 -> 7 -> 3 -> 5` and `k = 2`, it should become `3 -> 5 -> 7 -> 7`.

Given the linked list `1 -> 2 -> 3 -> 4 -> 5` and `k = 3`, it should become `3 -> 4 -> 5 -> 1 -> 2`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_11_Problem_177_Rotate_Linked_List.py)

## Problem 178

This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_12_Problem_178_Probalistic_Game.py)

## Problem 179

This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence `2, 4, 3, 8, 7, 5`, you should construct the following tree:

```
    5
   / \
  3   7
 / \   \
2   4   8
```

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_13_Problem_179_Reconstruct_Binary_Search_Tree.py)

## Problem 180

This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is `[1, 2, 3, 4, 5]`, it should become `[1, 5, 2, 4, 3]`. If the stack is `[1, 2, 3, 4]`, it should become `[1, 4, 2, 3]`.

Hint: Try working backwards from the end state.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_14_Problem_180_Interleave_Stack.py)

## Problem 181

This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string `racecarannakayak`,

return `["racecar", "anna", "kayak"]`.

Given the input string `abc`, return `["a", "b", "c"]`.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/2019_07_15_Problem_181_Least_Palindromes_Split.py)

## Problem 182

This problem was asked by Facebook.

A graph is minimally connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.

You can choose to represent the graph as either an adjacency matrix or adjacency list.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/problem_182_minimally_connected.py)

## Problem 183

This problem was asked by Twitch.

Describe what happens when you type a URL into your browser.

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/problem_183_url_request.md)

## Problem 184

This problem was asked by Amazon.

Given `n` numbers, find the greatest common denominator between them.

For example: given the numbers `[42, 56, 14]`, return `14`

[Solution](https://github.com/BaoCaiH/Daily_Coding_Problem/blob/master/Python/problem_184_largest_common_denominator.py)
