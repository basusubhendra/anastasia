#!/usr/bin/python3
import sys
from characterize import *
from pi import pi
from e import e

def factorize(sv, pp, ee):
    pass

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    state_vector1 = characterize(l, pi)
    state_vector2 = characterize(l, e)
    print(state_vector1)
    print(state_vector2)
    _state_vector_1_pi = factorize(state_vector1, pi, e)
    _state_vector_1_e = factorize(state_vector1, e, pi)
    _state_vector_2_pi = factorize(state_vector2, pi, e)
    _state_vector_2_e = factorize(state_vector2, e, pi)
