#!/usr/bin/python3
import sys
from pi import pi
from e import e
from _zeros import zeros

def read(f, zz):
    pp = ""
    ctr = 0
    f.seek(0)
    while ctr < zz:
        c = str(f.read(1))
        ctr = ctr + 1
        pp = pp + c
    return pp

def characterize(num, l, pp):
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    pp_index = 0
    state_vector_pp = 0 
    state_vector = []
    hit2 = 0
    while hit2 < l:
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
        if state_vector_pp in zeros:
            hit2 = hit2 + 1
            state_vector.append(state_vector_pp)
    return state_vector

def factorize(num, pp):
    l = len(num)
    state_vector = characterize(num, l, pp)
    return state_vector

num=str(sys.argv[1])
print("Number Entered was: " + str(num))
state_vector = factorize(num, pi)
print(state_vector)
