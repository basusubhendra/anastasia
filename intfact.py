#!/usr/bin/python3
import sys
from mpmath import *
from pi import pi
from e import e
from zeros import zeros

def characterize(num, l, pp, s):
    pp_index = 0
    state_vector_pp = []
    net_maturity = 0
    while True:
        hit = 0
        base_ctr = 0
        while True:
            ctr = 0
            pz = pi[:(base_ctr + ctr + 1)]
            ez = e[:(base_ctr + ctr + 1)][::-1]
            maturity = 0
            for x in list(zip(pz, ez)):
                if x[0] == x[1]:
                    maturity = maturity + 1
            index = pp.index(str(maturity)[::-1])
            if index == pp_index:
                net_maturity = net_maturity + maturity
                hit = hit + 1
                pp_index = pp_index + len(str(maturity))
                ctr = ctr + 1
                base_ctr = 0
                state_vector_pp.append(pz)
                if hit % l == 0:
                    break
            else:
                base_ctr = base_ctr + l
        if net_maturity in zeros:
            zidx = []
            init_index = 0
            while True:
                idx = zeros.index(net_maturity, init_index)
                zidx.append(idx)
                init_index = idx + 1
                if not net_maturity in zeros[init_index:]:
                    break
            zetazeros = []
            mp.prec = 64
            mp.dps = 64
            for x in zidx:
                zetazeros.append(str(zetazero(zidx[0]+1).imag))
            input([zidx, net_maturity, zetazeros])
        """
        else:
            print("Not Mature Yet")
            """

def factorize(num, pp, s):
    l = len(num)
    factor = characterize(num, l, pp, s)
    return factor

num=str(sys.argv[1])
print("Number Entered was: " + str(num))
c = num.count("0")
s = sum(map(int, num)) + 10*c
print("Sum of digits : " + str(s))
state_vector1 = factorize(num, pi, s)
state_vector2 = factorize(num, e, s)
print(state_vector1)
print(state_vector2)
