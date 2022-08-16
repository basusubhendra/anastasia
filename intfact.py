#!/usr/bin/python3
import sys
from mpmath import *

if __name__ == "__main__":
    mp.prec = 512
    mp.dps = 512
    num = str(sys.argv[1])
    print("Number entered was : " + str(num))
    base_ctr = 0
    init_zero_index = 1
    OPT_LEN = 5
    BLOCK_OFFSET = 0
    OFFSET = 0
    zero_index = init_zero_index
    _exit_ = False
    count = 0 
    while True:
        l = len(num)
        line = str(zetazero(zero_index).imag).split(".")
        zero = int(line[0]) 
        sieve = str(line[1])[BLOCK_OFFSET:BLOCK_OFFSET + 5]
        ctr = (base_ctr + zero - 1) % l
        start_index = (ctr + OFFSET*OPT_LEN) % l
        end_index = (start_index + OPT_LEN) % l
        i = start_index
        matches = []
        while True:
            nk = num[i % l]
            if nk in sieve:
                if nk == '0':
                    matches.append(10)
                else:
                    matches.append(int(nk))
            i = i + 1
            if i % l == end_index:
                break
        sumx = sum(matches)
        count = count + sumx
        if sumx == 0:
            input([BLOCK_OFFSET, OFFSET, count])
            BLOCK_OFFSET = BLOCK_OFFSET + 5
            OFFSET = OFFSET + 1
            if ctr > 0 and ctr % l == 0:
                _exit_ = True
            count = 0
        else:
            count = count + 1
    #        print([zero, sieve])
            pass
        zero_index = zero_index + sumx
        if _exit_ == True:
            break
    f.close()
