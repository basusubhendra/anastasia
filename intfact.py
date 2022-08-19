#!/usr/bin/python3
import sys
from pi import pi
from e import e
from zeros import zeros

pi10=['3','0','1','4','1','5','9','2','6','5']
e10=['2','0','7','1','8','2','8','1','8','2']
OPT_LEN = 5
def factorize(num):
    global pi10
    global e10
    global OPT_LEN
    rnum = num[::-1]
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
    last_hit1 = 0
    last_hit2 = 0
    counter = 1
    hit = 0
    states = []
    while True:
        c = str(f.read(1))
        d = str(g.read(1))
        parity1 = 0
        parity2 = 0
        if (t[0] == 0 and c == e10[cnt1]) or (t[0] == 1 and c == pi10[cnt1]):
               cnt1 = cnt1 + 1
               nk1 = nk1 - 1
               if nk1 == 0:
                   cnt1 = 0
                   t[0] = 1 - t[0]
                   last_hit1 = ctr1 % l
                   ctr1 = ctr1 + 1
                   nk1 = int(num[ctr1 % l])
                   if nk1 == 0:
                       nk1 = 10
                   parity1 = 1
        if (t[1] == 1 and d == pi10[cnt2]) or (t[1] == 0 and d == e10[cnt2]):
               cnt2 = cnt2 + 1
               nk2 = nk2 - 1
               if nk2 == 0:
                   cnt2 = 0
                   t[1] = 1 - t[1]
                   last_hit2 = ctr2 % l
                   ctr2 = ctr2 + 1
                   nk2 = int(num[ctr2 % l])
                   if nk2 == 0:
                       nk2 = 10
                   parity2 = 1
        if parity1 == 1 and parity2 == 1:
            hit = hit + 1
            if last_hit1 == last_hit2 and (last_hit1 + 1)  == counter:
                if (hit + OPT_LEN) in zeros:
                    states.append(hit+OPT_LEN)
                   # input("pi-e hit" + "\t" + str(hit))
                    if counter == l:
                        f.close()
                        g.close()
                        return states
                    counter = counter + 1
        elif parity1 == 1 and parity2 == 0:
            pass
        elif parity1 == 0 and parity2 == 1:
            pass
        elif parity1 == 0 and parity2 == 0:
            pass

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    states = factorize(num)
    print(states)
    #print("num = " + factor1 + " X " + factor2)
