#!/bin/python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for i in sys.argv[::-1]:
        if i is not sys.argv[0]:
            print(i)
