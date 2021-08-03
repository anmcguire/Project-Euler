#!/usr/bin/env python3

with open("../data/p022_names.txt", "r") as file:
    list = eval("[" + file.read() + "]")

total = i = 0
n = ord('A') - 1

for name in sorted(list):
    i  += 1
    total += sum([ord(c) - n for c in name]) * i
    
print(total)