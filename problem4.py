#!/usr/bin/env python

def isPalindrome(num):
    rev_num = int(str(num)[::-1])

    return (num - rev_num) == 0

x = range(100, 999)
y = range(100, 999)

palindromes = []

for _x in x:
    for _y in x:
        prod =  _x * _y

        if isPalindrome(prod): 
            palindromes.append(prod)

palindromes.sort()
print palindromes[-1]





    
