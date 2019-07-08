#!/usr/bin/env python3
#-*- coding: utf-8 -*-


# 往空数组，插入10个数据
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list = []
for i in range(10):
    num_list.append(i)
print(num_list)

# 随机生成长度为10的字符串
import random
name = ''
for i in range(10):
    tmp = random.randint(0, 25) + ord('a')
    name += chr(tmp)
print(name)

# 使用map(dict)保存学生信息
stu = {}
stu['name'] = input('please input your name: ')
stu['age'] = int(input('please input your age: '))
print(stu)  # 输出dict内容
print('for k in stu')
for k in stu:  #等同于 for k in stu.keys()
    print(k)
print('for k in stu.values()')
for v in stu.values():
    print(v)
print('for k,v in stu.items()')
for k,v in stu.items():
    print('k: ', k, 'v: ', v)



