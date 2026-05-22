#!/bin/python3

import sys


def downcase_it(string: str) -> str:
    return string.lower()


if len(sys.argv) < 2:
    print("none")
for i in sys.argv[1:]:
    print(downcase_it(i))
