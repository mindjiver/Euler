#!/usr/bin/env python

from operator import mul

# 1 and all primes below n = 20 are neccessary
primes = [2, 3, 5, 7, 11, 13, 17, 19]
n = 20
factors = set()
proper = []

def factorize(n):
    """
    Naive and slow factorization.
    """
    factors = [1]

    if n == 1: return factors

    for p in primes:
        if n % p == 0:
            factors.append(p)

    prod = reduce(mul, factors)

    if n != prod:
        factors.extend(factorize(n / prod))

    factors.remove(1)

    return sorted(factors)

# get all factors for all numbers up until n
for i in range(1, n+1):
    for f in factorize(i):
        factors.add(f)

# find the largest exponent for each factor, really ugly
for f in factors:
    if f == 1:
        continue
    e = 2
    s = f
    while(s < n):
        s = f**e
        e += 1

    for i in range(0, e-2):
        proper.append(f)
    print str(f) + " => " + str(f) + "**" + str(e-2)

print reduce(mul, proper)
