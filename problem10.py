#!/usr/bin/env python

def sieve_primes(num):

    numbers = range(2, num+1)
    primes = [2]
    p = 2
    index = 0

    while(p < num):

        r = range(p, num+1, p)
        r.remove(p)

        # should work!
        numbers = [n for n in numbers if n not in r]

        try:
            p = numbers[index]
            index += 1
        except IndexError:
            return numbers

    return numbers

# 300 000 = 1min
#n = 2000000
n = 5000
p = sieve_primes(n)
print sum(p)
