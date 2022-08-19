#!/usr/bin/python3
import sys
from pi import pi
from e import e
from zeros import zeros
from primes import primes

pi10=['3','0','1','4','1','5','9','2','6','5']
e10=['2','0','7','1','8','2','8','1','8','2']
def factorize(num):
    global pi10
    global e10
    l = len(num)

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    factorize(num)
