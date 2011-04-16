#!/usr/bin/env python
#n = 1   => 1
#n = 2   => 2
#n = 4   => 6
#n = 5   => 28
#n = 6   => 36
#n = 11  => 120
#n = 12  => 528
#n = 15  => 150
#n = 22  =>
#n = 30  => 2016
#n = 40  => 5460
#n = 50  => 25200
#n = 100 => 73920
#n = 130 => 2031120
#n = 261 => 17907120
#n = 313 => 76576500
#n = 551 => ?

n = 5
i = 0
s = i

while(True):
    i += 1
    # just add onto the previous sum.
    s += i

    # always divisable with 1 and self
    divs = 2
    for j in range(2, i):
        if s % j == 0:
            divs += 1

    print str(s) + ":\t" + str(divs)

    if divs >= n:
        print "Found it! " + str(divs)
        break
