#!/usr/bin/env python

# < deficient
# = perfect
# > abundant

def divisors(n):

    divs = []

    if n == 1:
        divs = [1]
        print str(divs) + " divides " + str(n)
        return divs

    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    print str(divs) + " divides " + str(n)
    return divs

#n  = 28123
n = 20

abundant = []

for i in range(1, n+1):
    div_sum = sum(divisors(i))

    if div_sum > i:
        abundant.append(i)

for i in range(1, n+1):
    print "Checking " + str(i)
    a = False
    for j in abundant:
        if i - j in abundant:
            a = True
            break

    if a == False:
        print str(i) + " is not a sum of two abundant #."
