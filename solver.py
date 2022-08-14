#!/usr/bin/python3
import sys
def solver(zz_set, num):
    ctr = 0
    l = len(num)
    _l = len(zz_set)
    cnt = 0
    nk = int(num[ctr % l])
    col_count = 1
    snippet = []
    _exit_ = False
    hit_ctrs = []
    while True:
        zk = zz_set[cnt % _l]
        i_index = -1
        prev_index = -1
        while nk > 0:
           if "0" in zk[i_index+1:]:
               prev_index = i_index
               i_index = zk.index("0", i_index + 1)
               if prev_index > -1 and i_index == prev_index + 1:
                   if not (ctr % l) in hit_ctrs:
                       snippet.append(col_count)
                       hit_ctrs.append(ctr % l)
                       input([col_count, ctr % l])
                       col_count = 1
                   else:
                       _exit_ = True
                       break
           nk = nk - 1
        if _exit_ == True:
            break
        if nk == 0:
           ctr = ctr + 1
           nk = int(num[ctr % l])
        if not "0" in zk[i_index + 1:]:
            cnt = cnt + 1
            if cnt % _l == 0:
                col_count = col_count + 1
    return snippet[::-1]
