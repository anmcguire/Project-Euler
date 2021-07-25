#!/usr/bin/env python

def sum_of_squares(n): 
    return (n * (n + 1) * (2 * n + 1)) / 6

def square_of_sum(n): 
    return (( n * (n + 1)) / 2) ** 2

print(int(square_of_sum(100) - sum_of_squares(100)))
