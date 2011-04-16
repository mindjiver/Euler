#!/usr/bin/env python

def sum_squares(num):
    sum = 0
    i = 0

    while(i<=num):
        sum += (i*i)
        i += 1

    return sum

def square_sum(num):

    s = sum(range(1, num+1))
    prod = s * s

    return prod

num = 100

s_sq = sum_squares(num)
sq_s = square_sum(num)

print str(sq_s) + " - " + str(s_sq) + " = ", 
print sq_s - s_sq
