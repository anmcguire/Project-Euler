#!/usr/bin/env python3

import math

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return(False)
    return(True)


print(sum(filter(lambda x: is_prime(x), range(1, int(2E6) + 1))))