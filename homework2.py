#!/usr/bin/env python
#-*- coding:  utf8 -*-
# 当输入的不是数字时，这个就报错了
num1 = input('please input the first number: ' )
num1 = int(num1)
num2 = input('please input the second number: ' )
num2 = int(num2)
print('%d %% %d= %d' % (num1, num2, num1 % num2))
print('%d / %d= %d' % (num1, num2, num1 / num2))

