#!/usr/bin/env python
#-*-coding: utf8 -*-
score = input('please input your score:')
score = int(score)
if score > 90 and score <= 100:
	print('优秀')
elif score > 80 and score <= 90:
	print('良好')
	print('加油')
elif score > 60 and score <= 80:
	print('合格')
else:
	print('不合格')
