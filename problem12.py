#!/usr/bin/env python

import sys

#n = 130 => 2031120 (2.234u)
#n = 200 => 
#n = 261 => 17907120
#n = 313 => 76576500
#n = 551 => ?

n = 130

# to feed a start value we need:
# - number of iterations
# - sum of all numbers
i = 0
s = i

while(True):

    d = list()
    divs = 0

    check_range = range(1, s+1)
#    print "checking " + str(i)
    for j in check_range:

        if s % j == 0:
            d.append(j)
            divs += 1
#            if j != 1:
#                # calculate all multipels of j in range(j, s+1)            
#                mult = map(lambda x: x*j, range(1, s+1))
#                mult = [x for x in mult if x in check_range]
#                print "multiples of " + str(j) + " " + repr(mult)
#                for m in mult:
#                    check_range.remove(m)
#            else:
#                check_range.remove(j)
#                mult = [j]
#
#            d.extend(mult)
#            divs += len(d)

    print str(s) + " has " + str(divs)
#    print "divisors " + str(d)
    
    if divs >= n:
        sys.exit()
    
    i = i + 1
    s += i
