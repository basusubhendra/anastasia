#!/usr/bin/python3
import sys

def factorize(num):
    l = len(num)
    f = open("./pi.txt","r")
    g = open("./e.txt", "r")
    ctr = 0
    _nk1 = num[ctr % l]
    _nk2 = num[(ctr + 1) % l]
    f.close()
    g.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    factorize(num)
