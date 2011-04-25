#!/usr/bin/env python

def fib(n):
    #Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    fn = 0
    fn1 = 0
    fn2 = 1

    for i in range(1, n+1):

        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn

    return str(fn)

i = 1

while(True):
    fn = fib(i)
    if len(fn) >= 1000:
        print "F" + str(i) + ": " + str(len(fn))
        break
    i += 1
