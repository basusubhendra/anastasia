#!/usr/bin/python3
import sys
import time
from characterize import *
from pi import pi
from e import e

def compute(_pp, _ee, n1, n2):
    pass

def factorize(num, sv, pp, ee):
    pass

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    print("Start of Characterization Phase")
    print(" ")
    start = time.process_time()
    state_vector1 = characterize(l, pi)
    end = time.process_time()
    print("End of Pi Characterization")
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Characterization Phase")
    print(state_vector1)
    print(" ")
    print(" ")
    print("Start of Factorization Phase")
    print(" ")
    start = time.process_time()
    _state_vector_1_pi = factorize(num, state_vector1, pi, e)
    print(_state_vector_1_pi)
    print("End of Pi-E Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Factorization Phase")
