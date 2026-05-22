#!/bin/python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    if sys.argv[1] >= sys.argv[2]:
        print("Not valid Input")
    else:
        tmp = []
        j = 0
        for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
            tmp.append(i)
        print(tmp)
