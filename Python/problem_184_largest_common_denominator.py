#!/usr/bin/env python
# coding: utf-8
"""2020 March 09 - Daily Coding Problem #184."""
# <markdown>
# ## 2020 March 09 - Daily Coding Problem #184
#
# This problem was asked by Amazon.
#
# Given `n` numbers, find the greatest common denominator between them.
#
# For example: given the numbers `[42, 56, 14]`, return `14`


# %%
primes = [2]


def is_prime(number):
    """Check whether the number is a prime."""
    # As a mathematic principle,
    # if a number is not divisible to any number
    # from 2 to its square-root,
    # It's a prime
    for n in range(2, int(number**0.5)+1):
        if number % n == 0:
            return False
    return True


def next_prime():
    """Find the next prime in the number line."""
    # Start searching from the largest known prime to save time
    n = primes[-1] + 1
    while not is_prime(n):
        n += 1
    # If found, add it to the global list and return
    primes.append(n)
    return n


def get_factors(number):
    """Get all the prime factors of the number."""
    factors = {}
    divider = number
    # First search in the known primes
    # Keep dividing the number to each prime
    # until the divider is not divisible by that prime anymore
    # Then move on to the next known prime
    for prime in primes:
        if prime > divider:
            break
        if divider % prime == 0:
            factors[prime] = 0
        else:
            continue
        remainder = 0
        while remainder == 0:
            factors[prime] += 1
            divider = divider / prime
            remainder = divider % prime
    # If after the prime and the divider is still not 1
    # Find the next prime in the number line
    # and repeat the above process until the quotient is 1 and remainder is 0
    while divider != 1:
        prime = next_prime()
        if divider % prime == 0:
            factors[prime] = 0
        else:
            continue
        remainder = 0
        while remainder == 0:
            factors[prime] += 1
            divider = divider / prime
            remainder = divider % prime
    return factors


def greatest_common_divisor(numbers):
    """Return the greatest common divisor of the given numbers."""
    gcd = {}
    for number in numbers:
        # Add the first number factors as the base gcd
        if not gcd:
            factor = get_factors(number)
            gcd = factor.copy()
        # For each of the next numbers
        # Check if each prime factor of the gcd is available
        # in the factors of that number
        # If yes, choose the lesser amount of that prime
        # If not, set that prime factor to 0
        else:
            factor = get_factors(number)
            for prime in gcd.keys():
                if prime not in factor.keys():
                    gcd[prime] = 0
                else:
                    gcd[prime] = min([gcd[prime], factor[prime]])
    n_gcd = 1
    for key, value in gcd.items():
        n_gcd = n_gcd * (key ** value)
    return n_gcd


# %%
n_lst = input('Give a list of number, separated by spaces: ')

n_lst = [int(n) for n in n_lst.split(' ')]
print(n_lst)

gcd = greatest_common_divisor(n_lst)
print(
    'The greatest common divisor is {}'.format(
        gcd
    ),
    'with each quotient as follow {}'.format(
        [n/gcd for n in n_lst]
    )
)
