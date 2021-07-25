#!/usr/bin/env python

import math

def factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n / i)
    return factors

print(max(filter(lambda x: len(factors(x)) == 2, [x for x in factors(600851475143)])))
