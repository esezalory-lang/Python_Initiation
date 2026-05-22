#!/bin/python3

import sys

# def shrink(string):
#     for i in range(0, 8):
#         print(string[i], end="")
#     print()

# def enlarge(string):
#     length = len(string)
#     for i in range(length, 8):
#         string += 'Z'
#     print(string)


def shrink(string):
    return string[:8]


def enlarge(string):
    string += "ZZZZZZZZZ"
    return string[:8]


if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) >= 8:
            print(shrink(i))
        elif len(i) < 8:
            print(enlarge(i))
