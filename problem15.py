#!/usr/bin/env python

from math import factorial

def permutations(n, k):
    #
    # n choose m = n! / k!(n-k)!
    #
    return factorial(n) / (factorial(k) * factorial(n - k))
    
#
# n = 2
#
# We need to cover 4 blocks to reach the destination, for this we need
# to walk 2 east and 2 south in any combination.
#
# 
n = 20
print permutations(n*2, n)
