#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

sanjiao = []
n = random.randint(1, 20)

for r in list(range(n)):
    left = ''
    for i in list(range(n - 1 - r)):
        left += ' '
    mid = ''
    for i in list(range(r * 2 + 1)):
        mid += '*'
    sanjiao.append(left + mid + left)

for elem in sanjiao:
    print(elem)

idx = len(sanjiao) - 2
while idx >= 0:
    print(sanjiao[idx])
    idx -= 1

