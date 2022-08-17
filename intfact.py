#!/usr/bin/python3
import sys

RUN_LENGTH=3
def characterize(num):
    l = len(num)
    pos = 0
    offsets = []
    while True:
        _nn = ""
        ctr = pos
        while ctr < pos + RUN_LENGTH:
            _nn = _nn + num[ctr % l]
            ctr = ctr + 1
        input(_nn)
        offsets.append(_nn)
        if ctr % l == 0:
            break
        pos = pos + RUN_LENGTH + l
    return offsets

if __name__ == "__main__":
    num = str(sys.argv[1])
    print("Number Entered was: " + str(num))
    triplets = characterize(num)
    print(triplets)

