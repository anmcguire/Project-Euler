#!/usr/bin/env python

import math

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return(False)
    return(True)

def nth_prime(n):
    i = j = 0
    while j != n:
        i += 1
        if is_prime(i):
            j += 1
        
    return(i)

print(nth_prime(10001))