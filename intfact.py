#!/usr/bin/python3
import sys
from pi import pi
from e import e

def characterize(num, l, pp, s):
    cnt = 0
    base_ctr = 0
    state_vector_pp = []
    pp_index = 0
    while True:
        ctr = 0
        pz = pi[:(base_ctr + ctr + 1)]
        ez = e[:(base_ctr + ctr + 1)][::-1]
        maturity = 0
        for x in list(zip(pz, ez)):
            if x[0] == x[1]:
                maturity = maturity + 1
        index = pp.index(str(maturity))
        if index == pp_index:
            pp_index = pp_index + len(str(maturity)) + 1
            cnt = cnt + 1
            ctr = ctr + 1
            state_vector_pp.append(pz)
            if ctr % l == 0:
                break
        else:
            base_ctr = base_ctr + l
    lsp = len(state_vector_pp)
    _ee = e[:lsp][::-1]
    _pp = pi[:lsp]
    _maturity = 0
    for x in list(zip(_pp, _ee)):
        if x[0] == x[1]:
            _maturity = _maturity + int(x[0])
    print(_maturity)
    sys.exit(2)
    
def factorize(num, pp):
    l = len(num)
    factor = characterize(num, l, pp, sum(map(int, num)))
    return factor

num=str(sys.argv[1])
print("Number Entered was: " + str(num))
state_vector1 = factorize(num, pi)
state_vector2 = factorize(num, e)
print(state_vector1)
print(state_vector2)
