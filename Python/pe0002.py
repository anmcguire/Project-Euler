#!/usr/bin/env python

def fib(a, b, max, list):
    if a + b < max:
        list.append(a + b)
        fib(b, a + b, max, list)
    return list

print(sum(filter(lambda x: x % 2 == 0, fib(0, 1, 4E6, []))))
