#!/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    tmp = input("What was the parameter? ")
    if len(re.findall(tmp, sys.argv[1])) == 0:
        print("Nope, sorry...")
    else:
        print("Good job!")
