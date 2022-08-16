#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num = str(sys.argv[1])
    l = len(num)
    print("Number entered was : " + str(num))
    base_ctr = 0
    init_zero_index = 1
    OPT_LEN = 5
    zero_index = init_zero_index
    f=open("./zeros.txt","r")
    f.seek(zero_index - 1)
    _exit_ = False
    while True:
        zz = f.readline(1).rstrip()
        zs = str(zz).split(".")
        zero = int(zs[0])
        sieve = zs[1]
        ctr = (base_ctr + zero - 1) % l
        start_index = (ctr + 1) % l
        end_index = (start_index + OPT_LEN) % l
        i = start_index
        matches = []
        count = 0 
        while True:
            nk = num[i % l]
            if nk in sieve:
                if nk == '0':
                    matches.append(10)
                else:
                    matches.append(int(nk))
            i = i + 1
            if i % l == end_index:
                break
        sumx = sum(matches)
        if sumx == 0:
            zero_index = init_zero_index
            base_ctr = base_ctr + zero - 1 
            if base_ctr % l == 0:
                _exit_ = True
        else:
            if len(matches) == 5:
                snippet.push(count)
                count = 1
            else:
                count = count + 1
            zero_index = zero_index + sumx
        if _exit_ == True:
            break
    f.close()
