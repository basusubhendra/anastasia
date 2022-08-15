#!/usr/bin/python3
import sys
from latest import *
_num = num[::-1]
_num1 = []
_num2 = []
t = 0
for x in list(zip(num, _num)):
    if t == 0:
        _num1.append(x[0])
        _num2.append(x[1])
    elif t == 1:
        _num1.append(x[1])
        _num2.append(x[0])
    t = 1 - t
ctr = 0
vec1 = []
vec2 = []
while ctr < len(_num1) - 1:
    vec1.append(_num1[ctr] + _num1[ctr + 1])
    vec2.append(_num2[ctr] + _num2[ctr + 1])
    ctr = ctr + 1
print(vec1)
print(vec2)
