#!/usr/bin/env python

#          10397494 function calls (10386487 primitive calls) in 3805.851 CPU seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000 3805.851 3805.851 <string>:1(<module>)
# 23382/12375 3776.252    0.162 3776.856    0.305 problem12.py:23(factorize)
#         1    4.852    4.852 3805.850 3805.850 problem12.py:3(<module>)
#     12375    0.211    0.000 3777.159    0.305 problem12.py:45(divisors)
#         1   18.694   18.694   19.682   19.682 problem12.py:7(sieve_primes)
#         1    0.001    0.001 3805.851 3805.851 {execfile}
#  10066933    1.009    0.000    1.009    0.000 {len}
#    121964    0.106    0.000    0.106    0.000 {method 'append' of 'list' objects}
#     54559    0.024    0.000    0.024    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     11007    0.012    0.000    0.012    0.000 {method 'extend' of 'list' objects}
#     23381    0.047    0.000    0.047    0.000 {method 'remove' of 'list' objects}
#     12376    2.910    0.000    2.910    0.000 {range}
#     35756    0.279    0.000    0.279    0.000 {reduce}
#     23381    0.208    0.000    0.208    0.000 {sorted}
#     12375    1.246    0.000    1.246    0.000 {sum}



from operator import mul
import sys

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

# from problem05.py
def factorize(n):
    """
    Naive and slow factorization.
    """
    factors = [1]

    if n <= 0: return []
    if n == 1: return factors

    for p in primes:
        if n % p == 0:
            factors.append(p)

    prod = reduce(mul, factors)

    if n != prod:
        factors.extend(factorize(n / prod))

    factors.remove(1)

    return sorted(factors)

def divisors(n):
    # n = a^n + b^m + ... + c^q 
    # divisors = (n + 1) * (m + 1) + (q + 1)    

    # 2, 2, 5, 5, 5, 7, 11, 13
    # =>
    # get exponent of primes
    # 2 3 1 1 1 
    # =>
    # 3 4 2 2 2
    # return reduce(mul, prime_exponents)

    f = factorize(n)

    i = 0
    exps = []

    while i < len(f):
        c = f.count(f[i])
        i = i + c
        exps.append(c)

    exps = [n + 1 for n in exps]

    return reduce(mul, exps)

i = 1
divs = 500

# get all the primes < n
n = 10000000
p = sieve_primes(n)
primes = [n for n in range(2, n) if p[n] == True]

while(True):
    n = sum(range(1, i + 1))
    d = divisors(n)

    print str(n) + " : " + str(d)
    
    if d > divs:
        print n
        break

    i += 1
