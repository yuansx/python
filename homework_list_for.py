#!/usr/bin/env python
#-*- coding: utf8 -*-

score_list = [100, 60, 89, 75, 99, 94, 23]

sum = 0
for score in score_list:
    sum += score

print(sum / len(score_list))

info = {"name": "逗比", "age": 23, 'money': 10000}

for k,v in info.items():
    print('key: ' + str(k))
    print('value: ' + str(v))
    print('---------------')

for value in info.values():
    print(value)
print('---------------')
for key in info.keys():
    print(str(key) + ':' + str(info[key]))
