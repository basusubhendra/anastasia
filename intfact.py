#!/usr/bin/python3
import sys
from zeros1 import zeros1
from characterize import *
from solver import *

if __name__ == "__main__":
    num = str(sys.argv[1])
    ctr = 1
    s0 = ""
    s1 = ""
    while True:
        print("==== " + str(ctr-1) + "=====")
        zz = characterize(int(ctr), pi)
        _zz = zz + 1
        if ctr == 1:
            s0 = int(zz)
            ctr = ctr + 1
            continue
        else:
            s1 = int(zz)
        zz_set = []
        if s0 <= s1:
            for x in range(s0, s1 + 1):
                zz = str(zeros1[x])
                zz_set.append(zz)
        elif s0 > s1:
            for x in range(s0, s1 - 1, -1):
                zz = str(zeros1[x])
                zz_set.append(zz)
            zz_set = zz_set[::-1]
        snippet = int(solver(zz_set, num))
        input(snippet % 7)
        ctr = ctr + 1 
        s0 = int(s1)
        if ctr % 7 == 0:
            print(" ")
            print(" ")
