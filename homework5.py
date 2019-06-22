#!/usr/bin/env python
#-*- coding: utf8 -*-

import random

array = []

for idx in list(range(10)):
    tmp = random.randint(1, 100)
    array.append(tmp)

print(array)
