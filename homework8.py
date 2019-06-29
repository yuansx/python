#!/usr/bin/env python
#-*- coding: utf8 -*-

import random
i=0
num = []
while i < 10:
    num.append(random.randint(1,100))
    i +=1
print(num)

i = 0
while i < len(num):
    j = i + 1
    while j < len(num):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
        j += 1
    i += 1

print(num)

