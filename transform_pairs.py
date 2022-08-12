#!/usr/bin/python3
def transform_pairs(num, p):
    l = len(num)
    stats = []
    for x in range(0, int(l / 2) + 1):
        n1 = num[x]
        n2 = num[-(x + 1)]
        if p == 0:
           nn = n1 + n2
           stats.append(nn)
        else:
           nn = n2 + n1
           stats.append(nn)
    if p == 1:
       stats = stats[::-1]
    return stats
