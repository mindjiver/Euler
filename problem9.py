#!/usr/bin/env python
# coding=utf8

#naive solution:
# 
# brute force find all tuples (a,b,c) for which a+b+c = 1000
# brute-force triplet(a,b,c)


# O(n**3) :D
#for a in range(1, n):
#    for b in range(1, n):
#        for c in range(1, n):
#            if ((a + b + c) - n) == 0:
#                l.append((a,b,c))

def triplet(a, b, c):

    if ((a*a + b*b) - c*c) == 0:
        return True
    else:
        return False


#Take any m and n, such that m>n and then find: 2mn, m² − n², m² + n².
# O(?) n**2 here?
for m in range(1, 1000):
    for n in range(1, m):

        if n == 0:
            continue

        a = (m * m) - (n * n)
        b = 2 * m * n
        c = (m * m) + (n * n)
    
        t = (a,b,c)

        if(a+b+c == 1000):
            print a*b*c
