#!/usr/bin/python3
import sys
from pi import pi
from e import e

pi10=['3','0','1','4','1','5','9','2','6','5']
e10=['2','0','7','1','8','2','8','1','8','2']

def complement11(num):
    c11 = ""
    for x in num:
        c11 = c11 + str((11-int(x)) % 10)
    return c11

def _analyze(num, num11, sums):
    ctr = 0
    s0 = sums[ctr]
    ctr = ctr + 1
    success = False
    cnt = 0
    l = len(num)
    pivots = []
    while ctr < len(sums):
        s = sums[ctr]
        delta = s - s0
        if delta > 0 and delta == int(num11[cnt]):
            s0 = s
            cnt = cnt + 1
            pivots.append(ctr)
            if cnt == l:
                return True, pivots
        elif delta < 0 and abs(delta) == int(num[cnt]):
            s0 = s
            cnt = cnt + 1
            pivots.append(ctr)
            if cnt == l:
                return True, pivots
        ctr = ctr + 1
    return False, None

def analyze(num, pi_hits, e_hits, pp, ee):
    sums = []
    for x in list(zip(pp, pi_hits, e_hits, ee)):
        sums.append(int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]))
    num11 = complement11(num)
    success, pivots = _analyze(num, num11, sums[::-1])
    input([sums, success])
    if success == True:
        input(pivots)
        return success

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
    pi_hits = []
    e_hits = []
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
            pi_hits.append(num[ctr1 % l])
            e_hits.append(num[ctr2 % l])
            hit = hit + 1
            pp = pi[:hit]
            ee = e[:hit][::-1]
            success = analyze(num, pi_hits, e_hits, pp, ee)
            if success == True:
                sys.exit(0)
            """
            #success, bin_factor1, bin_factor2 = analyze(pi_hits, e_hits, pp, ee)
            if success == True:
                return int(bin_factor1), int(bin_factor2)
            """

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    factor1, factor2 = factorize(num)
    print("num = " + factor1 + " X " + factor2)
