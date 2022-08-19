#!/usr/bin/python3
import sys

OPT_LEN=8
def factorize(num):
    global OPT_LEN
    l = len(num)
    f = open("./pi.txt","r")
    g = open("./e.txt", "r")
    ctr = 0
    cnt = 0
    _nk = num[ctr % l]
    _ee = ""
    posits = []
    pos = 0
    while True:
        nk = num[cnt % l]
        c = str(f.read(1))
        d = str(g.read(1))
        _ee = _ee + d
        if c == nk:
            posits.append(pos)
            cnt = cnt + 1
            if d == _nk:
                ctr = ctr + 1
                _nk = num[ctr % l]
                if ctr % l == 0 and int(ctr / l) == OPT_LEN:
                    break
        pos = pos + 1
    _ee = _ee[::-1]
    pivots = []
    for x in posits:
        pivots.append(int(_ee[x]))
    print(pivots)
    f.close()
    g.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    factorize(num)
