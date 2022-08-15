#!/usr/bin/python3
import sys
f = open("./zeros6","r")
g = open("./zeros.txt","w")
lines = f.readlines()
for line in lines:
    l = str(line).lstrip().rstrip().split(".")
    ss = l[0]
    ss = ss + "." + l[1][:5]
    g.write(ss)
    g.write("\n")
g.close()
f.close()

