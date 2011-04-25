#!/usr/bin/env python

def divisors(n):

    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
            
    return divs

div_sums = dict()
n = 10000

for i in range(2, n):
    div_sums[i] = sum(divisors(i))

amic_pairs = list()

for (k, v) in div_sums.iteritems():
    try:
        # not very pretty, last one removes duplicates.
        if k == div_sums[v] and k != v and (v,k) not in amic_pairs:
            amic_pairs.append((k, v))

    except KeyError:
        pass

sum = 0

for (a,b) in amic_pairs:
    sum += a + b

print sum
