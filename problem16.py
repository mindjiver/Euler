#!/usr/bin/env python

s = 1
for i in range(1000): s *= 2
s = map(int, str(s))

print sum(s)
