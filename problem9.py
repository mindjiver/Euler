#!/usr/bin/env python
# coding=utf8

import sys

#naive solution:
# 
# brute force find all tuples (a,b,c) for which a+b+c = 1000
# brute-force triplet(a,b,c)
#
#def triplet(a, b, c):
#
#    if ((a*a + b*b) - c*c) == 0:
#        return True
#    else:
#        return False
#
# O(n**3) :D
#for a in range(1, n):
#    for b in range(1, n):
#        for c in range(1, n):
#            if ((a + b + c) - n) == 0:
#                l.append((a,b,c))
#


#Take any m and n, such that m>n and then find: 2mn, m² − n², m² + n².
# O(?) n**2 here?
sum = 1000

for m in range(1, sum+1):
    for n in range(1, m):

        if n == 0:
            continue

        a = (m * m) - (n * n)
        b = 2 * m * n
        c = (m * m) + (n * n)
    
        t = (a,b,c)

        if(a+b+c == sum):
            print a*b*c
            sys.exit()
