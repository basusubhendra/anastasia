#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros1.py","w")
g.write("zeros1=[")
lines = f.readlines()
for line in lines:
    l = str(line).lstrip().rstrip()[:8].replace(".","")
    g.write(str(l) + ",")
g.write("]")
g.close()
f.close()
