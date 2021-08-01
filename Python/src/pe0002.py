#!/usr/bin/env python3

def recrel_to_max(a, b, max, list):
    if a + b < max:
        list.append(a + b)
        recrel_to_max(b, a + b, max, list)
    return list

print(sum(filter(lambda x: x % 2 == 0, recrel_to_max(0, 1, 4E6, []))))
