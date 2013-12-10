#!/usr/bin/env python

import sys
import math

def primes(num):
    i = 1
    primes = []

    while(i <= num):
        i += 1

        # skip all odd numbers.
        if i != 2 and i % 2 == 0:
            continue

        d = False
        for n in primes:
            if i % n == 0:
                d = True

        if d == False:
            primes.append(i)
            yield i

i = 1
for p in primes(1000000):
    print str(i) + " : " + str(p)
    if i == 10001:
        sys.exit()
    i += 1
