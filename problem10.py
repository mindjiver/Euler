#!/usr/bin/env python

def sieve_primes(num):

    numbers = set(range(2, num+1))
    primes = [2]
    p = 2
    
    while(p < num):
        
        #slow, optimize
        r = set(range(p, num+1, p))
        numbers = numbers - r

        if len(numbers) > 0:
            # convert back to sorted list to read head element.
            # slow, optimize
            p = sorted(list(numbers))[0]
            primes.append(p)
        else:
            return sorted(list(primes))

    return sorted(list(primes))

def eratosthenes_sieve(m):
    # Create a candidate list within which non-primes will be
    # marked as None; only candidates below sqrt(m) need be checked. 
    candidates = range(m+1)
    fin = int(m**0.5)
 
    # Loop over the candidates, marking out each multiple.
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue
 
        candidates[2*i::i] = [None] * (m//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

# 300 000 = 1min
n = 2000000
#p = sieve_primes(n)
#print p
p = eratosthenes_sieve(n)
print sum(p)
