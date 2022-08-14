#!/usr/bin/python3
import sys
from zeros1 import zeros1
from characterize import *
from solver import *

if __name__ == "__main__":
    num = str(sys.argv[1])
    n = len(num)
    stats = []
    _stats = []
    for x in range(1, int(n) + 1):
        stats.append(characterize(int(x), pi))
        _stats.append(characterize(int(x), pi) + 1)
    print(stats)
    print(_stats)
    ctr = 0
    s0 = stats[ctr]
    _stats = []
    while ctr < len(stats) - 1:
        print("<<<< " + str(ctr + 1) + " <<<< ")
        s1 = stats[ctr + 1]
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
        solver(zz_set, num)
        ctr = ctr + 1 
        s0 = stats[ctr]
        print(" ")
