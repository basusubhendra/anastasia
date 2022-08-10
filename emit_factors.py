#!/usr/bin/python3
import sys
from pi import pi
from e import e
from zeros import zeros
MAX_LIMIT = 100
num = str(sys.argv[1])
f=open("./output.txt","r")
line=f.readlines()
s=line[0].split(",")[:-1]
ctr = 0
result1 = []
result2 = []
while ctr < len(s):
    s0 = int(s[ctr])
    s_1 = int(s[-(ctr + 1)])
    ctr = ctr + 1
    pp = pi[s0:s0 + MAX_LIMIT]
    ee = e[s_1:s_1 + MAX_LIMIT]
    pp = e[s0:s0 + MAX_LIMIT]
    ee = pi[s_1:s_1 + MAX_LIMIT]
