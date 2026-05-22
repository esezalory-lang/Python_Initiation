#!/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")
