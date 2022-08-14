#!/usr/bin/python3
import sys
from mpmath import *
from _zeros import zeros
from pi import pi
from e import e

MAX_DIGITS = 8
def read(f, zz):
    pp = ""
    ctr = 0
    f.seek(0)
    while ctr < zz:
        c = str(f.read(1))
        ctr = ctr + 1
        pp = pp + c
    return pp

def characterize(l, pp):
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    pp_index = 0
    state_vector_pp = 0 
    state_vector = []
    while True:
        hit = 0
        base_ctr = 0
        while True:
            ctr = 0
            pz = read(fp, (base_ctr + ctr + 1))
            ez = read(fe, (base_ctr + ctr + 1))[::-1]
            maturity = 0
            for x in list(zip(pz, ez)):
                if x[0] == x[1]:
                    maturity = maturity + 1
            maturity = maturity % 10
            index = pp.index(str(maturity)[::-1], pp_index)
            if index == pp_index:
                hit = hit + 1
                pp_index = pp_index + len(str(maturity))
                ctr = ctr + 1
                base_ctr = 0
                state_vector_pp = state_vector_pp + len(pz)
                if hit == l:
                    break
            else:
                base_ctr = base_ctr + l
        _ee = e[:state_vector_pp]
        _pp = pi[:state_vector_pp]
        net_maturity = 0
        for m in list(zip(_pp, _ee)):
            if m[0] == m[1]:
                 net_maturity = net_maturity + 1
        if net_maturity in zeros:
            return zeros.index(net_maturity) + 1

if __name__ == "__main__":
    n = int(sys.argv[1])
    num = ""
    if len(sys.argv) >= 2:
       num = str(sys.argv[2])
    stats = []
    for x in range(1, int(n) + 1):
        stats.append(characterize(int(x), pi))
    print(stats)
    ctr = 0
    s0 = stats[ctr]
    while ctr < len(stats) - 1:
        s1 = stats[ctr + 1]
        if s0 <= s1:
            zz_set = []
            for x in range(s0, s1 + 1):
                zz = str(zetazero(x).imag)[:MAX_DIGITS]
                zz_set.append(zz)
            print(zz_set)
        elif s0 > s1:
            zz_set = []
            for x in range(s0, s1 - 1, -1):
                zz = str(zetazero(x).imag)[:MAX_DIGITS]
                zz_set.append(zz)
            print(zz_set)
        ctr = ctr + 1 
        s0 = stats[ctr]
        print(" ")
