#!/usr/bin/env python
# coding: utf-8
"""2019 April 26th - Daily_Coding_Problem #101."""
# <markdown>
# ## 2019 April 26th - Daily_Coding_Problem #101
#
# Problem: Given an even number (greater than 2),
# return two prime numbers whose sum will be equal to the given number.
#
# A solution will always exist. See Goldbach’s conjecture.
#
# Example:
#
# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible,
# return the lexicographically smaller solution.


# <codecell>
def isPrime(number):
    """Check if the given number is a prime."""
    for n in range(2, int(number**0.5) + 1):
        if number % n == 0:
            return False
    return True


def goldbachPair(number):
    """Return the 2 prime number whose sum is equal to the given number."""
    if number % 2 != 0:
        print("The given number is not an even number.")
        return None
    for n in range(2, number):
        if isPrime(n):
            if isPrime(number - n):
                return (n, number - n)


# %%
print(goldbachPair(int(input('Please give an even number:'))))
