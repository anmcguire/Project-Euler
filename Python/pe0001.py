#!/usr/bin/env python

def pe0001(n):
    return(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(n))))

print(pe0001(1000))
