#!/usr/bin/env python

units = {
    1:   "one",
    2:   "two",
    3:   "three",
    4:   "four",
    5:   "five",
    6:   "six",
    7:   "seven",
    8:   "eight",
    9:   "nine",
    10:  "ten",
    11:  "eleven",
    12:  "twelve",
    13:  "thirteen",
    14:  "fourteen",
    15:  "fifteen",
    16:  "sixteen",
    17:  "seventeen",
    18:  "eighteen",
    19:  "nineteen"
}

tens = {
    2:  "twenty",
    3:  "thirty",
    4:  "forty",
    5:  "fifty",
    6:  "sixty",
    7:  "seventy",
    8:  "eighty",
    9:  "ninety",
}

def num_to_string(n):
    # split n into parts:
    # e.g.
    # n = 1234
    # =>
    # 1000 200 30 4
    th = n / 1000
    h = (n - (th * 1000)) / 100
    t = (n - ((th * 1000) + (h * 100))) / 10
    u = n - ((th * 1000) + (h * 100) + (t * 10))

#    print (th, h, t, u)

    s = ""

    if n < 20:
        s += (units[n])
        return s

    if th > 0:
        s += units[th] + "thousand"
        if h > 0 or t > 0 or u > 0:
            s += "and"
        else:
            return s

    if h > 0:
        s += units[h] + "hundred"
        if t > 0 or u > 0:
            s += "and"
        else:
            return s

    if t > 0:
        if t == 1:
            s += units[10+u]
            return s

        s += tens[t]
        if u > 0:
            s += units[u]
        return s

    if u > 0:
        s += units[u]

    return s

c = 0

for n in range(1, 1001):
    s = num_to_string(n)
    print s
    c += len(s)

print c
