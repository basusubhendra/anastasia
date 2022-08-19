#!/usr/bin/python3
import sys
from pi import pi
from e import e

pi10=['3','0','1','4','1','5','9','2','6','5']
e10=['2','0','7','1','8','2','8','1','8','2']

def factorize(num):
    global pi10
    global e10
    l = len(num)
    ctr1 = 0
    ctr2 = 0
    nk1 = int(num[ctr1 % l])
    if nk1 == 0:
        nk1 = 10
    nk2 = int(num[ctr2 % l])
    if nk2 == 0:
        nk2 = 10
    cnt1 = 0
    cnt2 = 0
    t = [0, 1]
    f = open("./pi.txt","r")
    g = open("./e.txt","r")
    counter = 0
    t3 = 0
    reconstructed_number = ""
    hit = 0
    mid = int(l / 2)
    pi_vector = []
    e_vector = []
    pi_ones = 0
    e_ones = 0
    while True:
        c = str(f.read(1))
        d = str(g.read(1))
        parity1 = 0
        parity2 = 0
        finished_nk1 = ""
        finished_nk2 = ""
        if (t[0] == 0 and c == e10[cnt1]) or (t[0] == 1 and c == pi10[cnt1]):
               cnt1 = cnt1 + 1
               nk1 = nk1 - 1
               if nk1 == 0:
                   finished_nk1 = num[ctr1 % l]
                   cnt1 = 0
                   t[0] = 1 - t[0]
                   ctr1 = ctr1 + 1
                   nk1 = int(num[ctr1 % l])
                   if nk1 == 0:
                       nk1 = 10
                   parity1 = 1
        if (t[1] == 1 and d == pi10[cnt2]) or (t[1] == 0 and d == e10[cnt2]):
               cnt2 = cnt2 + 1
               nk2 = nk2 - 1
               if nk2 == 0:
                   finished_nk2 = num[ctr2 % l]
                   cnt2 = 0
                   t[1] = 1 - t[1]
                   ctr2 = ctr2 + 1
                   nk2 = int(num[ctr2 % l])
                   if nk2 == 0:
                       nk2 = 10
                   parity2 = 1
        if parity1 == 1 and parity2 == 1:
            pi_vector.append(pi_ones)
            e_vector.append(e_ones)
            pi_ones = 0
            e_ones = 0
            if hit == mid:
                return pi_vector, e_vector
            hit = hit + 1
        elif parity1 == 1 and parity2 == 0:
            pi_ones = pi_ones + 1
        elif parity1 == 0 and parity2 == 1:
            e_ones = e_ones + 1
        elif parity1 == 0 and parity2 == 0:
            pass

def emit_factors(pv, ev, num):
    pass

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    pv, ev = factorize(num)
    print(pv)
    print(ev)
    #factor1, factor2 = emit_factors(pv, ev, num)
    #print("num = " + factor1 + " X " + factor2)
