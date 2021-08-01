#!/usr/bin/env python3

print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))
