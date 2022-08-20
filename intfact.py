#!/usr/bin/python3
import sys

def factorize(num):
    l = len(num)
    f = open("./pi.txt","r")
    #slowest running counter
    ctr = 0
    #fast running counter
    count = 0
    _pivots = []
    while ctr < l - 1:
        _nk1 = num[ctr % l]
        _nk2 = num[(ctr + 1) % l]
        cnt = 0
        nk = num[cnt % l]
        hit = 0
        #pi digit specific counter
        pivots = []
        target = ctr 
        f.seek(0)
        while True:
            c = str(f.read(1))
            __nk = num[count % l]
            if c == nk:
                cnt = cnt + 1
                nk = num[cnt % l]
                if cnt % l == 0:
                    hit = hit + 1
                if __nk == num[target % l] and cnt % l == 0:
                    pivots.append(hit)
                    if target == ctr + 1:
                        count = count + 1
                        break
                    target = ctr + 1 
            count = count + 1
        _pivots.append(pivots)
        ctr = ctr + 1
    f.close()
    return _pivots

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    pivots = factorize(num)
    print(pivots)
