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
    acc1 = []
    acc2 = []
    _acc1 = [nk1]
    _acc2 = [nk2]
    prev_pos1 = -1
    prev_pos2 = -1
    pos1 = 0
    pos2 = 0
    while True:
        c = str(f.read(1))
        d = str(g.read(1))
        input([c, d])
        parity1 = 0
        parity2 = 0
        finished_nk1 = ""
        finished_nk2 = ""
        if (t[0] == 0 and c == e10[cnt1]) or (t[0] == 1 and c == pi10[cnt1]):
               cnt1 = cnt1 + 1
               nk1 = nk1 - 1
               if nk1 == 0:
                   cnt1 = 0
                   t[0] = 1 - t[0]
                   ctr1 = ctr1 + 1
                   nk1 = int(num[ctr1 % l])
                   if nk1 == 0:
                       nk1 = 10
                   parity1 = 1
                   c = str(f.read(1))
                   _pos = f.tell()
                   if (t[0] == 0 and c == e10[cnt1]) or (t[0] == 1 and c == pi10[cnt1]):
                       _acc1.append(num[ctr1 % l]) 
                       parity1 = 0
                       cnt1 = cnt1 + 1
                       nk1 = nk1 - 1
                       if nk1 == 0:
                            cnt1 = 0
                            t[0] = 1 - t[0]
                            ctr1 = ctr1 + 1
                            nk1 = int(num[ctr1 % l])
                            if nk1 == 0:
                                nk1 = 10
                            parity1 = 1
                   else:
                       _acc1 = [ nk1]
                       f.seek(_pos-1, 0)
                   acc1.append(_acc1)
                   _acc1 = []
        if (t[1] == 1 and d == pi10[cnt2]) or (t[1] == 0 and d == e10[cnt2]):
               cnt2 = cnt2 + 1
               nk2 = nk2 - 1
               if nk2 == 0:
                   cnt2 = 0
                   t[1] = 1 - t[1]
                   ctr2 = ctr2 + 1
                   nk2 = int(num[ctr2 % l])
                   if nk2 == 0:
                       nk2 = 10
                   parity2 = 1
                   d = str(g.read(1))
                   _pos = g.tell()
                   if (t[1] == 1 and d == pi10[cnt2]) or (t[1] == 0 and d == e10[cnt2]):
                       _acc2.append(num[ctr2 % l]) 
                       parity2 = 0
                       cnt2 = cnt2 + 1
                       nk2 = nk2 - 1
                       if nk2 == 0:
                            cnt2 = 0
                            t[1] = 1 - t[1]
                            ctr2 = ctr2 + 1
                            nk2 = int(num[ctr2 % l])
                            if nk2 == 0:
                                nk2 = 10
                            parity2 = 1
                   else:
                       _acc2 = [ nk2]
                       g.seek(_pos-1, 0)
                   acc2.append(_acc2)
                   _acc2 = []
        if parity1 == 1 and parity2 == 1:
            input("pi-e hit")
        elif parity1 == 1 and parity2 == 0:
            input("pi_hit")
        elif parity1 == 0 and parity2 == 1:
            input("e_hit")
        elif parity1 == 0 and parity2 == 0:
            pass
        pos1 = pos1 + 1
        pos2 = pos2 + 1

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    factor1, factor2 = factorize(num)
    #print("num = " + factor1 + " X " + factor2)
