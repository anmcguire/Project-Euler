#!/usr/bin/env python3

file = open("../data/p067_triangle.txt", "r")

i = 0
m = []

for line in file.readlines():
    m.append([])
    for s in line.split():
        m[i].append(int(s))
    i += 1

file.close()

dim = max([len(k) for k in m])

for k in m:
    n = dim - len(k)
    if n > 0:
        k += [ 0 ] * n

for i in range(dim - 2, -1, -1):
    for j in range(i + 1):
        if m[i + 1][j] > m[i + 1][j + 1]:
            m[i][j] += m[i + 1][j]
        else:
            m[i][j] += m[i + 1][j + 1]
            
print(m[0][0])
