#!/usr/bin/python3
import sys
def solver(zz_set, num):
    ctr = 0
    l = len(num)
    _l = len(zz_set)
    cnt = 0
    nk = int(num[ctr % l])
    col_count = 1
    zk = zz_set[cnt % _l]
    cols = []
    sumx = 0
    last_ctr = 0
    while True:
        i_index = -1
        reset = False
        while nk > 0:
           reset = False
           if "0" in zk[i_index+1:]:
               i_index = zk.index("0", i_index + 1)
           else:
               cnt = cnt + 1
               if cnt % _l == 0:
                   reset = True
                   delta = ctr - last_ctr
                   sumx = sumx + delta
                   y = input(float(sumx / l))
                   if y == 'y':
                       return None
                   last_ctr = ctr
                   col_count = col_count + 1
               zk = zz_set[cnt % _l]
           nk = nk - 1
        cols.append(col_count)
        ctr = ctr + 1
        if reset == True and ctr % l == 0:
            break
        nk = int(num[ctr % l])
    return col_count
