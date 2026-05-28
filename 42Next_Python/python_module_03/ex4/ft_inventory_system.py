#!/bin/python3

import sys


def inventory_parser(input: list) -> dict:
    inventory = {}
    for pair in input:
        key, value = pair.split(":")
        inventory[key] = value
    print(inventory)




if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory_parser(sys.argv[1::])
