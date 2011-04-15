#!/usr/bin/env python

def mult(x, y): return x * y

def find_divisors(composite):
    i = 1
    factors = []
    max = composite
    while(i <= max):
        if composite % i == 0:
            factors.append(i)
            max = composite / i

        i = i + 1

    return factors

def factorize(n):
    
    i = 1
    factors = []

    while(i < n):
        
        if (n % i)  == 0:
            factors.append(i)
            
        i = i + 1

    return factors

#composite = 13195
composite = 600851475143

divisors = find_divisors(composite)
factors = []

for d in reversed(divisors):
    
    if len(factorize(d)) == 1:
        factors.append(d)

print str(factors) + " are primes in " + str(reduce(mult, factors))
