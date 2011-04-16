#!/usr/bin/env python

#n -> n/2     (n is even)
#n -> 3n + 1 (n is odd)

# optimization: store all calculated chains, always check the n
# towards the head of all chains, if the the same number, dont
# calculate the chain again, just append it.

def iter_seq(n, seq):
    seq.append(n)

    if n == 1:
        return seq

    if n % 2 == 0:
        iter_seq(n / 2, seq)
    else:        
        iter_seq(3*n + 1, seq)

n = 1000000
max = 0
l = []
longest = []

for i in range(1, n+1):
    print "Calculating " + str(i)
    l = []
    iter_seq(i, l)
    if len(l) > max:
        max = len(l)
        longest = l

print longest
print max

