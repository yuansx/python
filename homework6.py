#!/usr/bin/env python
#-*- coding: utf-8 -*-
scores = []
while True:
    score = input()
    if score == 'end':
        break
    if not score.isdigit():
        continue
    scores.append(int(score))
sum = 0
for score in scores:
    sum += score
print(sum)
aver = sum/len(scores)
print(aver)
nu = []
perfect_num = 0
for score in scores:
    if score > aver:
        perfect_num += 1
        nu.append(score)
print(nu)
C = len(nu)/len(scores)
percent = perfect_num / len(scores)
print(C)
print(percent)



