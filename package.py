#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 第一种做法
#import random
#print(random.randint(1,10))

# 第2种做法
#from random import randint
#print(randint(1, 100))

# 第3种做法
#from random import *
#print(randint(20, 30))

# 第4种做法
#from random import randint as rint
#print(rint(2, 22))

# 第5种做法
#import random as rd
#print(rd.randint(11, 22))

import function

if __name__ == '__main__':
    print(function.add(12, 34))
    print('in package, __name__ is ', __name__)

