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
    zero_index = init_zero_index
    _exit_ = False
    count = 0 
    while True:
        l = len(num)
        line = str(zetazero(zero_index).imag).split(".")
        zero = int(line[0]) 
        sieve = str(line[1])[BLOCK_OFFSET:BLOCK_OFFSET + 5]
        ctr = (base_ctr + zero - 1) % l
        start_index = (ctr + 1) % l
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
        if sumx == 0:
            BLOCK_OFFSET = BLOCK_OFFSET + 5
            if ctr > 0 and ctr % l == 0:
                _exit_ = True
            input([BLOCK_OFFSET, count])
            count = 0
        else:
    #        print([zero, sieve])
            count = count + 1
        zero_index = zero_index + sumx
        if _exit_ == True:
            break
    f.close()
