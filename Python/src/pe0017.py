#!/usr/bin/env python3

import re
import inflect

total = 0
p = inflect.engine()

for i in range(1, 1001):
    list = re.split(r'[-\s+]', p.number_to_words(i))
    total += sum([len(s) for s in list])
    
print(total)