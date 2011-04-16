#!/usr/bin/env python

from operator import mul

n = reduce(mul, range(1, 100))
s = 0
for c in str(n):
    s += int(c)

print str(s)
