#!/usr/bin/python3
import sys
import time
from characterize import *
from pi import pi
from e import e

def factorize(num, sv, pp, ee):
    cnt = 0
    stats = []
    _stats = []
    for x in sv:
        n1 = num[cnt]
        n2 = num[-(cnt + 1)]
        nn = n2 + n1
        print(nn)
        ns = ""
        if int(nn) < 10:
            ns = int(nn) + 100
        else:
            ns = int(nn) 
        xs = str(x)[-2:]
        if int(xs) < 10:
            xs = int(xs) + 100
        else:
            xs = int(xs)
        _pp = pp[:xs]
        _ee = ee[:xs][::-1]
        ctr = 0
        stats = []
        while ctr < xs:
            sum_xs = 0
            _ctr = ctr
            while _ctr < xs:
                ps = 0
                if int(_pp[_ctr]) == 0:
                    ps = 10
                else:
                    ps = int(_pp[_ctr])
                es = 0
                if int(_ee[_ctr]) == 0:
                    es = 10
                else:
                    es = int(_ee[_ctr])
                sum_xs = sum_xs + ps
                sum_xs = sum_xs + es
                if sum_xs >= ns:
                    break
                _ctr = _ctr + 1
            if sum_xs == ns:
                stats.append([ctr, _ctr])
            ctr = ctr + 1
        _stats.append(stats)
        cnt = cnt + 1
    print(_stats)

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    print("Start of Characterization Phase")
    print(" ")
    start = time.process_time()
    state_vector1 = characterize(l, pi)
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Characterization Phase")
    print(state_vector1)
    print(" ")
    print(" ")
    print("Start of Factorization Phase")
    print(" ")
    start = time.process_time()
    factorize(num, state_vector1, pi, e)
    #_state_vector_1_pi = factorize(num, state_vector1, pi, e)
    #print(_state_vector_1_pi)
    print("End of Pi-E Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Factorization Phase")
