#!/usr/bin/python3
import sys
from t_300 import t

l = len(t)
m = int(l/2)
ss = []
for x in range(0, m):
    ss.append([t[x], t[-(x+1)]])
print(ss)
