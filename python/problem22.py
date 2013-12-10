#!/usr/bin/env python

with open("names.txt") as f:
    names = f.read()

names = names.replace("\"", "")
names = sorted(names.split(","))

sum = 0

for name in names:
    s = 0
    index = names.index(name) + 1
    l = [ord(c) - 64 for c in name]
    for i in l: s += i
#    print name + " : " + str(s) + " * " + str(index) + " = " + str(s * (index))
    sum += s * index

print sum
