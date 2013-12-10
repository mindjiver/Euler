#!/usr/bin/env python

prev = 1
elem = 2

seq = [1, 2]

while(1):
    tmp = elem
    elem = elem + prev
    prev = tmp

    if elem < 4000000:
        seq.append(elem)
    else:
        break

even = [x for x in seq if x % 2 == 0]

print even
print sum(even)
