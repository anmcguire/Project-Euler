#!/usr/bin/env python

def collatz(n, list):
    list.append(n)
    if n == 1:
        return(list)
    if n % 2 == 0:
        return(collatz(int(n / 2), list))
    else:
        return(collatz(int(3 * n + 1), list))

largest = 0
answer = 1

for i in range(1, int(1E6)):
    length = len(collatz(i, []))
    if length > largest:
        largest = length
        answer = i

print(answer)
