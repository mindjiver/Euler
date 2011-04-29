#!/usr/bin/env python

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

n = 2000000
p = sieve_primes(n)
print sum([n for n in range(2, n) if p[n] == True])
