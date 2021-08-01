#!/usr/bin/env python3

import math

def factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors += [i, n / i]
    return(factors)

print(max(filter(lambda x: len(factors(x)) == 2, [x for x in factors(600851475143)])))
