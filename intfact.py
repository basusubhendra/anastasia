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
    l = len(num)
    mid = int(l / 2)
    while ctr < (len(sv) - 1):
       s2 = sv[ctr + 1]
       if s2 >= s1:
           t = 1
       elif s2 < s1:
           t = -1
       nn = ""
       if s1 < s2:
           n1 = num[-(ctr + 1)]
           n2 = num[-(ctr + 2)]
           if ctr <= mid:
               nn = n2 + n1
           else:
               nn = n1 + n2
       elif s1 > s2:
           n1 = num[ctr]
           n2 = num[ctr + 1]
           if ctr <= mid:
               nn = n1 + n2
           else:
               nn = n2 + n1
       p =0
       for x in range(s1, s2+t, t):
           _pp = pp[:x]
           _ee = ee[:x][::-1]
           sum_x = 0
           print(p+1)
           print(_pp)
           print(_ee)
           p = p + 1
           print(s1, s2, nn)
           input("Enter")
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
               if sum_x >= int(nn):
                   break
       if sum_x == int(nn):
           stats.append(ctr)
       ctr = ctr + 1
       s1 = sv[ctr]
    print(stats)
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
    time1 = end - start
    print("Time Taken = " + str(end-start))
    print(state_vector1)
    """
    print(" ")
    start = time.process_time()
    state_vector2 = characterize(l, e)
    end = time.process_time()
    time2 = end - start
    print("Time Taken = " + str(end-start))
    print(state_vector2)
    print(" ")
    print("Total Time Taken = " + str(time1 + time2))
    """
    print("End of Characterization Phase")
    print(" ")
    print(" ")
    print("Start of Factorization Phase")
    print(" ")
    start = time.process_time()
    factorize(num, state_vector1, pi, e)
    #_state_vector_1_pi = factorize(num, state_vector1, pi, e)
    #print(_state_vector_1_pi)
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    """
    start = time.process_time()
    factorize(num, state_vector2, pi, e)
    #_state_vector_1_pi = factorize(num, state_vector1, pi, e)
    #print(_state_vector_1_pi)
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print(" ")
    """
    print("End of Factorization Phase")
