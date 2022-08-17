#!/usr/bin/python3
import sys
from mpmath import *

PREC=128
RUN_LENGTH=3
OPT_LEN=5
def characterize(num):
    global OPT_LEN
    global RUN_LENGTH
    l = len(num)
    pos = 0
    offsets = []
    state_vec = []
    while True:
        _nn = ""
        ctr = pos
        while ctr < pos + RUN_LENGTH:
            _nn = _nn + num[ctr % l]
            ctr = ctr + 1
        offsets.append(_nn)
        _nn = ""
        while ctr < pos + RUN_LENGTH + OPT_LEN:
            _nn = _nn + num[ctr % l]
            ctr = ctr + 1
        state_vec.append(_nn)
        if ctr % l == 0:
            break
        pos = pos + RUN_LENGTH
    return offsets,state_vec

def _calculate_(l, bit_pattern):
    global OPT_LEN
    print("Input: " + str(bit_pattern))
    ctr = 0
    acc = ""
    nn = bit_pattern[ctr]
    if nn == 1:
        acc = str(nn)
    ctr = ctr + 1
    _acc_ = 0
    while ctr < OPT_LEN:
        nn = bit_pattern[ctr]
        input("nn = " + str(nn))
        if acc:
            print(acc, int(acc, 2))
        if acc != "" and nn == 1:
            acc = acc + str(nn)
        elif acc == "" and nn == 1:
            acc = str(nn)
        elif acc == "" and nn == 0:
            pass
        elif (acc != "" and len(acc) > 0 and acc) and (nn == 0 or ctr == OPT_LEN-1):
            _acc_ = _acc_ + int(acc, 2)
            acc = ""
        ctr = ctr + 1
        input(acc)
    if acc and len(acc) > 0 and acc != "":
        print("Accumulator " + str(int(acc, 2)))
        _acc_ = _acc_ + int(acc, 2)
    return _acc_

def _match_(l, triplets, state_vec, param):
    f = ""
    if param == 0:
        f = open("./pi.txt","r")
    else:
        f = open("./e.txt","r")
    __bit_patterns__ = []
    for x in list(zip(triplets, state_vec)):
        chars = int(x[0])
        _bit_patterns_ = 0
        while True:
            if chars == 0:
                chars = 1000
            c = str(f.read(chars))
            ctr = 0
            bit_pattern = []
            sumx = 0
            while ctr < OPT_LEN:
                c = str(f.read(1))
                if c in x[1]:
                    _c = c
                    if int(c) == 0:
                        _c = 10
                    sumx = sumx + int(_c)
                    bit_pattern.append(1)
                else:
                    bit_pattern.append(0)
                ctr = ctr + 1
            input(bit_pattern)
            chars = chars + sumx
            _dec_ = _calculate_(l, bit_pattern)
            _bit_patterns_ = _bit_patterns_ + _dec_
            input("Bit Patterns " + str(_bit_patterns_))
            if chars % l  == 0: # position modulo L == 0
                __bit_patterns__.append(_bit_patterns_)
                break
            elif sumx == 0: #no match
                __bit_patterns__.append(_bit_patterns_)
                break
    return __bit_patterns__

def _convert_(sums):
    global PREC
    _states_ = []
    zero_index = 1
    mp.prec=PREC
    mp.dps=PREC
    for _sum_ in sums:
        zero  = str(zetazero(zero_index).imag)[_sum_]
        if zero == '.':
            zero = '0'
        _states_.append(int(zero))
        zero_index = zero_index + 1
    return _states_

if __name__ == "__main__":
    num = str(sys.argv[1])
    l = len(num)
    print("Number Entered was: " + str(num))
    #Characterization Phase
    triplets, state_vec = characterize(num)
    #Analysis Phase
    pi_sums = _match_(l, triplets, state_vec, 0)
    print(pi_sums)
    _zero_digits_pi_ = _convert_(pi_sums)
    #print(_zero_digits_pi_)
    e_sums = _match_(l, triplets, state_vec, 1)
    _zero_digits_e_ = _convert_(e_sums)
    #print(_zero_digits_e_)
