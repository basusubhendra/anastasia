#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros1.py","w")
h=open("./zeros2.py","w")
g.write("zeros1=[")
h.write("zeros2=[")
lines = f.readlines()
for line in lines:
    l = str(line).rstrip().split(".")
    if line != lines[-1]:
        g.write(str(l[0][-1])+",")
        h.write(str(l[1][0])+",")
    else:
        g.write(str(l[0][-1]))
        h.write(str(l[1][0]))
g.write("]")
h.write("]")
g.close()
h.close()
