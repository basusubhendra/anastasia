#!/usr/bin/python3
import sys
num = str(sys.argv[1])
rnum = num[::-1]
for x in list(zip(rnum, num)):
    print([x[0], x[1]])
