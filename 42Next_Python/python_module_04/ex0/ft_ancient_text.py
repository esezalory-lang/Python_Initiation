#!/bin/python3

import sys
# import typing


if __name__ == "__main__":
    open_error = False
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
        except Exception as e:
            open_error = True
            print(f"Error opening file '{sys.argv[1]}': {e}")
        if open_error is False:
            print("---\n")
            print(file.read())
            print("---")
            try:
                file.close()
            except Exception as e:
                print(f"Error closing file '{file}': {e}")
            print(f"File '{sys.argv[1]}' closed.")
