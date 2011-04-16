#!/usr/bin/env python

#end = 10 #2520  
         # 1, 2, 3, 4,  5, 6,  7, 8,    9,   10
         # 1  2  3  2*2 5  3*2 7  2*2*2 3*3  2*5 => 1, 2, 3, 5, 7

#end = 11 #27720
#end = 12 #27720
#end = 13 #360360 = 13 * 27720
#end = 14 #360360
#end = 15 #360360
#end = 16 #720720 = 360360
end = 20

divisors = range(1, end+1)

j = reduce(lambda x,y: x*y, divisors)
i = 87297210 # product of all primes in of reduce(lambda x,y: x*y, range(1, 20))
all_divs = []

while(i < j):

    print "\nchecking " + str(i) + ": ",
    divs = 0

    for d in reversed(divisors):
        if i % d == 0:
            divs = divs + 1

    d = divs
    while(d):
        print "*",
        d = d - 1
    print " (" + str(divs) + ")",

    if divs == end:
        print i
        all_divs.append(i)
        break

    i = i + 1

print all_divs
