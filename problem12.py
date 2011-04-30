#!/usr/bin/env python

from operator import mul

# from problem10.py
def sieve_primes(num):

    numbers = [True] * num;

    for n in xrange(2, num + 1):
        # Replace all True elements with False elements if they are
        # multiplies of a number in the range.
        #
        # len will be called 1999999 times for n = 2 000 000, not very
        # optimized.
        l = len(numbers[n*n::n])
        numbers[n*n::n] = l * [False]

    return numbers

def factorize(n):
    """
    Somewhat improved from problem 12 euler discussions.
    """
    factors = []

    if n <= 0: return []
    if n == 1: return factors

    while n > 1:
        for p in primes:
            if n % p == 0:
                factors.append(p)
                n = n / p 
                break

    return sorted(factors)

def divisors(n):
    # n = a^n + b^m + ... + c^q
    # factors = (n + 1) * (m + 1) + (q + 1)
    #
    # e.g. n = 500500
    #
    # 2, 2, 5, 5, 5, 7, 11, 13
    # get exponent of primes =>
    # 2 3 1 1 1
    # add 1 to all exponents =>
    # 3 4 2 2 2
    # calculate product of exponents =>
    # return reduce(mul, exps)

    f = factorize(n)

    i = 0
    exps = [0]

    while i < len(f):
        c = f.count(f[i])
        i = i + c
        exps.append(c)

    exps = [n + 1 for n in exps]

    return reduce(mul, exps)

i = 1
divs = 500

# get all the primes < n, program will get into a infinte loop if
# there is a prime factor larger than the list largest.
#
# n = 10 000 000 takes less than 20s.
n = 10000000
p = sieve_primes(n)
primes = [n for n in range(2, n) if p[n] == True]

while(True):
    n = sum(range(1, i + 1))
    d = divisors(n)

    if d > divs:
        print str(n) + " : " + str(d)
        break

    i += 1
