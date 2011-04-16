#!/usr/bin/env python

n = reduce(lambda x,y: x*y, range(1, 100))
s = 0
for c in str(n):
    s += int(c)

print str(s)
