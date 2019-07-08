#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def add(num1, num2):
    return num1 + num2, num1, num2


print('in function, __name__ is ', __name__)
if __name__ == '__main__':
    sum_num, num1, num2 = add(1, 2)
    print(sum_num)
    
    sum_num, _, _ = add(23, 2)
    print(sum_num)
    
    ret = add(4, 5)
    print(ret[0])
    
    print(add(2, 3))

