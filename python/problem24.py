#!/usr/bin/env python

# the number of permutations of a n length list is n!

from itertools import permutations, islice

# recipe from itertools library documentation.
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

l = range(0, 10)
n = 1000000

print take(n, permutations(l))[-1]
