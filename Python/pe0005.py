#!/usr/bin/env python3

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return abs((a * b) / gcd(a, b))

def pe0005(list):
     n = 1
     while len(list) > 0:
          n = lcm(n, list.pop(0))
     return(int(n))

print(pe0005(list(range(2, 21))))
