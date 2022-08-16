#!/usr/bin/python3
import sys
from math import *

def characterize(num, param, init_zero_index, MULT, OPT_LEN):
    zero_index = init_zero_index
    f = open("./zeros.txt", "r")
    _matches = []
    counter = 0
    while True:
        line = str(f.readline()).rstrip().split(".")
        for x in range(init_zero_index, zero_index - 1):
             line = str(f.readline()).rstrip().split(".")
        zero = int(line[0])
        sieve = str(line[1])
        offset = (zero - 1)
        start_index = (offset + OPT_LEN*(MULT-1))
        end_index = (start_index + OPT_LEN*MULT)
        ctr = start_index 
        matches = []
        nn = ""
        while ctr < end_index:
            nk = num[ctr % l]
            nn = nn + nk
            ctr = ctr + 1
        _sieve = []
        if param == 0:
            _sieve = sieve
        else:
            for ss in sieve:
                _sieve.append(str((11-int(ss)) % 10))
        matches = []
        for x in _sieve:
            if x in nn:
                matches.append(int(x))
        #print(matches)
        for m in matches:
            _matches.append(m)
        if len(matches) == 0:
            MULT = MULT + 1
            return set(sorted(_matches)), zero_index, MULT
        sumx = sum(matches)
        init_zero_index = zero_index + 1
        zero_index = zero_index + sumx
        counter = counter + 1

if __name__ == "__main__":
    num = str(sys.argv[1])
    l = len(num)
    print("Number entered was : " + str(num))
    rnum = num[::-1]
    _zero_index1 = 1
    _zero_index2 = 1
    _MULT1 = 1
    _MULT2 = 1
    _zero_index3 = 1
    _zero_index4 = 1
    _MULT3 = 1
    _MULT4 = 1
    pow2 = pow(2, x)
    while True:
        set1, zero_index1, MULT1 = characterize(rnum, 0, _zero_index1, _MULT1, OPT_LEN)
        _zero_index1 = zero_index1
        _MULT1 = MULT1
        set2, zero_index2, MULT2 = characterize(num, 1, _zero_index2, _MULT2, OPT_LEN)
        _zero_index2 = zero_index2
        _MULT2 = MULT2
        set3, zero_index3, MULT3 = characterize(num, 0, _zero_index3, _MULT3, OPT_LEN)
        _zero_index3 = zero_index3
        _MULT3 = MULT3
        set4, zero_index4, MULT4 = characterize(rnum, 1, _zero_index4, _MULT4, OPT_LEN)
        _zero_index4 = zero_index4
        _MULT4 = MULT4
        print(set1)
        print(" ")
        print(set2)
        print(" ")
        print(set3)
        print(" ")
        print(set4)
        print(" ")
        input("Enter")
