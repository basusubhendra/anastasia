#!/usr/bin/python3
import sys
import time
from characterize import *
from pi import pi
from e import e

def compute(_pp, _ee, n1, n2):
    hash_map_nr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    hash_map_dr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    sum_nr = 0
    sum_dr = 0
    delta = 0
    max1 = max(int(n1), int(n2))
    for x in list(zip(_pp, _ee)):
        found = False
        hash_map_nr[int(x[0])] = hash_map_nr[int(x[0])] + 1
        hash_map_dr[int(x[1])] = hash_map_dr[int(x[1])] + 1
        for y in range(0, 10):
            if hash_map_nr[y] <= max1:
                found = True
                break
        if found == False:
            return None
        for y in range(0, 10):
            if hash_map_dr[y] <= max1:
                found = True
                break
        if found == False:
            return None
        if x[0] == '0':
            sum_nr = sum_nr + 10
        else:
            sum_nr = sum_nr + int(x[0])
        if x[1] == '0':
            sum_dr = sum_dr + 10
        else:
            sum_dr = sum_dr + int(x[1])
        if hash_map_nr[int(x[0])] == int(n1) and hash_map_dr[int(x[1])] == int(n2):
            delta = [sum_nr , sum_dr]
            break
        elif hash_map_nr[int(x[1])] == int(n1) and hash_map_dr[int(x[0])] == int(n2):
            delta = [sum_dr , sum_nr]
            break
    return delta

MAX_LIMIT = 1000
def factorize(num, sv, pp, ee):
    global MAX_LIMIT
    l = len(sv)
    mid = int(l / 2)
    output = []
    for x in range(0, mid):
        s1 = sv[x]
        s2 = sv[-(x+1)]
        n1 = num[x]
        n2 = num[-(x+1)]
        _pp = pp[s1:s1+MAX_LIMIT]
        _ee = ee[s2:s2+MAX_LIMIT]
        delta = compute(_pp, _ee, n1, n2)
        output.append(delta)
    return output

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was : " + str(num))
    l = len(num)
    print("Start of Characterization Phase")
    start = time.process_time()
    state_vector1 = characterize(l, pi)
    end = time.process_time()
    print("End of Pi Characterization")
    print("Time Taken = " + str(end-start))
    start = time.process_time()
    state_vector2 = characterize(l, e)
    print("End of E Characterization")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print("End of Characterization Phase")
    print(state_vector1)
    print(state_vector2)
    print(" ")
    print(" ")
    print("Start of Factorization Phase")
    start = time.process_time()
    _state_vector_1_pi = factorize(num, state_vector1, pi, e)
    print(_state_vector_1_pi)
    print("End of Pi-E Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    start = time.process_time()
    _state_vector_1_e = factorize(num, state_vector1, e, pi)
    print(_state_vector_1_e)
    print("End of E-Pi Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print("End of Compute of Factor 1")
    start = time.process_time()
    _state_vector_2_pi = factorize(num, state_vector2, pi, e)
    print(_state_vector_2_pi)
    print("End of Pi-E Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    start = time.process_time()
    _state_vector_2_e = factorize(num, state_vector2, e, pi)
    print(_state_vector_2_e)
    print("End of E-Pi Factorization Phase")
    end = time.process_time()
    print("Time Taken = " + str(end-start))
    print("End of Compute of Factor 2")
    print("End of Factorization Phase")
    print(" ")
    print(" ")
