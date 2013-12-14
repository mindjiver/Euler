#!/usr/bin/env python

elem = 0
seq = [1, 2]

while(elem < 4000000):
    elem = seq[-1] + seq[-2]
    seq.append(elem)

even = [x for x in seq if x % 2 == 0]

print even
print sum(even)
