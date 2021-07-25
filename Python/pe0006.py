#!/usr/bin/env python

def sum_of_squares(n): 
    return (n * (n + 1) * (2 * n + 1)) / 6

def square_of_sum(n): 
    return (( n * (n + 1)) / 2) ** 2

def pe0006(n):
    return(square_of_sum(n) - sum_of_squares(n))

print(pe0006(100))
