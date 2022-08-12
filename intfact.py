#!/usr/bin/python3
import sys
import time
from characterize import *
from pi import pi
from e import e

def factorize(num, sv, pp, ee):
    ctr = 0
    s1 = sv[ctr]
    stats = []
    while ctr < (len(sv) - 1):
       s2 = sv[ctr + 1]
       if s2 >= s1:
           t = 1
       elif s2 < s1:
           t = -1
       #calculate condition from num
       #depending on whether s1 ><= s2
       for x in range(s1, s2+t, t):
           _pp = pp[:x]
           _ee = ee[:x][::-1]
           sum_x = 0
           for z in list(zip(_pp, _ee)):
               zs1 = 0
               zs2 = 0
               if int(z[0]) == 0:
                   zs1 = 10
               else:
                   zs1 = int(z[0])
               if int(z[1]) == 0:
                   zs2 = 10
               else:
                   zs2 = int(z[1])
               sum_x = sum_x + zs1 + zs2
               #condition here TBD
       #if condition
       stats.append(ctr)
       ctr = ctr + 1
       s1 = sv[ctr]
    return stats

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    print("Start of Characterization Phase")
    print(" ")
    start = time.process_time()
    state_vector1 = characterize(l, pi)
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Characterization Phase")
    print(state_vector1)
    print(" ")
    print(" ")
    print("Start of Factorization Phase")
    print(" ")
    start = time.process_time()
    factorize(num, state_vector1, pi, e)
    #_state_vector_1_pi = factorize(num, state_vector1, pi, e)
    #print(_state_vector_1_pi)
    print("End of Pi-E Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    print("End of Factorization Phase")
