#!/usr/bin/env python3

import math

def factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n / i))
    return factors

n = j = k = 0
while n <= 500:
    j += 1
    k += j
    n = len(factors(k))
print(k)

