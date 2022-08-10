#!/usr/bin/python3
import sys
from pi import pi
from e import e
from zeros import zeros

f=open("./output.txt","r")
line=f.readlines()
s=line[0].split(",")[:-1]
ctr = 0
result1 = []
result2 = []
while ctr < len(s):
    s0 = s[ctr]
    s_1 = s[-(ctr + 1)]
    ctr = ctr + 1
    pp = pi[s0:s0 + 1000]
    ee = e[s_1:s_1 + 1000]
    nr_zero = 0
    dr_zero = 0
    for x in list(zip(pp, ee)):
        if x[0] == '0':
            nr_zero = nr_zero + 1
        if x[1] == '0':
            dr_zero = dr_zero + 1
        if x[0] == x[1] and x[0] == '0':
            if nr_zero == dr_zero:
                result1.append(nr_zero)
                break
            else:
                print("not a semi prime")
                break
    pp = e[s0:s0 + 1000]
    ee = pi[s_1:s_1 + 1000]
    nr_zero = 0
    dr_zero = 0
    for x in list(zip(pp, ee)):
        if x[0] == '0':
            nr_zero = nr_zero + 1
        if x[1] == '0':
            dr_zero = dr_zero + 1
        if x[0] == x[1] and x[0] == '0':
            if nr_zero == dr_zero:
                result2.append(nr_zero)
                break
            else:
                print("not a semi prime")
                break
