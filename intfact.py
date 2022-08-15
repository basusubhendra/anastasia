#!/usr/bin/python3
import sys
from zeros1 import zeros1
from characterize import *
from solver import *
from primes import *

if __name__ == "__main__":
    num = str(sys.argv[1])
    ctr = 1
    s0 = ""
    s1 = ""
    nzeros = 0
    haves = 0
    have_nots = 0
    while True:
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
        #print(snippet % 7)
        if snippet % 7 == 0:
            nzeros = nzeros + 1
        if (ctr-1) % 7 == 0:
            print(" ")
            haves = haves + nzeros
            have_nots = have_nots + (7 - nzeros)
            print("==== " + str(ctr-1) + "=====")
            input(["nzeros =  " + str(nzeros), haves, have_nots, "zeros" , [haves in zeros, have_nots in zeros], "primes" , [haves in primes, have_nots in primes]])
            nzeros = 0
        ctr = ctr + 1 
        s0 = int(s1)
