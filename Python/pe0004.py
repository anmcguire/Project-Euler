#!/usr/bin/env python3


palindromes = []
r = range(999, 99, -1)

for i in r:
    for j in r:
        k = i * j
        if str(k) == str(k)[::-1]:
            palindromes.append(k)

print(max(palindromes))
