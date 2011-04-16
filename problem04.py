#!/usr/bin/env python

def isPalindrome(num):
    rev_num = int(str(num)[::-1])

    return (num - rev_num) == 0

palindromes = []
r = range(100, 999)

for x in r:
    for y in r:
        prod =  x * y

        if isPalindrome(prod): 
            palindromes.append(prod)

palindromes.sort()
print palindromes[-1]
    
