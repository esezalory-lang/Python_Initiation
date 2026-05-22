#!/bin/python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        if i.find("ism") == -1:
            print(i + "ism")
