#!/bin/python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    if len(re.findall(sys.argv[1], sys.argv[2])) == 0:
        print("none")
    else:
        print(len(re.findall(sys.argv[1], sys.argv[2])))
