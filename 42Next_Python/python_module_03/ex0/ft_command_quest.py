#!/bin/python3

import sys


if __name__ == "__main__":

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    for argument in sys.argv[1::]:
        print(f"Argument {i}: {argument}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}\n")
