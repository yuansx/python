#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json

stu = {'name': 'cony', 'age': 6}

print(stu)
stu_str = json.dumps(stu)
print(stu_str)
print(isinstance(stu_str, str))
print(isinstance(stu_str, dict))

dog_str = '{"name": "嘟嘟", "age": 1.5}'
print('dog_str', dog_str, ' is string? ', isinstance(dog_str, str))

dog = json.loads(dog_str)
print('dog ', dog, ' is string? ', isinstance(dog, str))
print('dog', dog, ' is dict? ', isinstance(dog, dict))

num_str = '[1, 2, 3]'
num_list = json.loads(num_str)
print(isinstance(num_list, list))

