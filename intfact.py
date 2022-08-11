#!/usr/bin/python3
import sys
from characterize import *
from pi import pi
from e import e

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    state_vector1 = characterize(l, pi)
    state_vector2 = characterize(l, e)
    print(state_vector1)
    print(state_vector2)
