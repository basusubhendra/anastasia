#!/usr/bin/python3
f=open("./zeros6","r")
lines=f.readlines()
g=open("./zeros.py","w")
g.write("zeros = [")
for line in lines:
    l = str(line).lstrip().rstrip().split(".")
    g.write(l[0])
    if line != lines[-1]:
       g.write(",")
g.write("]")
g.close()
f.close()
