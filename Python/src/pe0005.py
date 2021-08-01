#!/usr/bin/env python3

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return abs(int((a * b) / gcd(a, b)))

list = list(range(2, 21))
n = 1
while len(list) > 0:
    n = lcm(n, list.pop(0))

print(n)
