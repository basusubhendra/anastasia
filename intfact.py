#!/usr/bin/python3
import sys

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
    ctr = 0
    acc = ""
    nn = bit_pattern[ctr]
    if nn == 1:
        acc = str(nn)
    ctr = ctr + 1
    _acc_ = 0
    while ctr < OPT_LEN:
        nn = bit_pattern[ctr]
        if acc != "" and nn == 1:
            acc = acc + str(nn)
        elif acc == "" and nn == 1:
            acc = str(nn)
        elif (acc != "" and len(acc) > 0 and acc) and (nn == 0 or ctr == OPT_LEN-1):
            _acc_ = _acc_ + int(acc, 2)
            acc = ""
        ctr = ctr + 1
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
            chars = chars + sumx
            _dec_ = _calculate_(l, bit_pattern)
            _bit_patterns_ = _bit_patterns_ + _dec_
            if chars % l  == 0: # position modulo L == 0
                __bit_patterns__.append(_bit_patterns_)
                break
            elif sumx == 0: #no match
                __bit_patterns__.append(_bit_patterns_)
                break
    return __bit_patterns__

if __name__ == "__main__":
    num = str(sys.argv[1])
    l = len(num)
    print("Number Entered was: " + str(num))
    triplets, state_vec = characterize(num)
    #Characterization Phase
    #print(triplets)
    #print(state_vec)
    #Analysis Phase
    pi_sums = _match_(l, triplets, state_vec, 0)
    print(pi_sums)
    e_sums = _match_(l, triplets, state_vec, 1)
    print(e_sums)
