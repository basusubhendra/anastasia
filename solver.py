#!/usr/bin/python3
import sys
def solver(zz_set, num):
    prev_ctr = -1
    ctr = 0
    l = len(num)
    _l = len(zz_set)
    cnt = 0
    nk = int(num[ctr % l])
    col_count = 0
    snippet = []
    _exit_ = False
    while True:
        zk = zz_set[cnt % _l]
        i_index = -1
        prev_index = -1
        while nk > 0:
           if "0" in zk[i_index+1:]:
               prev_index = i_index
               i_index = zk.index("0", i_index + 1)
           else:
               break
           nk = nk - 1
        while nk == 0 and "0" in zk[i_index + 1:]:
           if prev_ctr == ctr:
               _exit_ = True
           prev_ctr = ctr
           ctr = ctr + 1
           nk = int(num[ctr % l])
           prev_index = i_index
           i_index = zk.index("0", i_index + 1)
           if prev_index > -1 and i_index == prev_index + 1:
               snippet.append(col_count)
               input(col_count)
               col_count = 0
           nk = nk - 1
        if not "0" in zk[i_index + 1:]:
            cnt = cnt + 1
            if cnt % _l == 0:
                col_count = col_count + 1
        if _exit_ == True:
            break
    return snippet[::-1]
