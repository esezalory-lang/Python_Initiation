#!/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    tmp = int(len(re.findall('z', sys.argv[1])))
    if tmp == 0:
        print("none")
    else:
        for i in range(0, tmp):
            print('z', end="")
        print()
