#!/usr/bin/env python

import math

def factors(n):
    list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            list.append(i)
    return list

def pe0003(n):
    return max(filter(lambda x: factors(x) == [1], [x for x in factors(n)]))

print(pe0003(600851475143))
