#!/usr/bin/python3
def transform_pair(num, p):
    l = len(num)
    for x in range(0, int(l / 2) + 1):
        n1 = num[x]
        n2 = num[-(x + 1)]
        if p == 0:
           nn = n1 + n2
           stats.append(nn)
        else:
           nn = n2 + n1
           stats.append(nn)
    if p == 0:
       print(stats)
    else:
       print(stats[::-1])
