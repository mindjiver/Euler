#!/usr/bin/env python

def sum_sqaures(num):
    sum = 0
    i = num

    while(i<=num):
        sum = sum + (i*i)

    return sum

print sum_sqaures(10)
