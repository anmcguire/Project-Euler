#!/usr/bin/env python


def pe0004():
    palindromes = []

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            k = i * j
            if str(k) == str(k)[::-1]:
                palindromes.append(k)

    return(max(palindromes))

print(pe0004())
