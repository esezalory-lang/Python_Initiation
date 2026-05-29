#!/bin/python3

import sys


def inventory_parser(input_inv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for pair in input_inv:
        split_worked = True
        try:
            item, quantity = pair.split(":")
            if item in inventory.keys():
                print(f"Redundant item '{item}' - discarding")
                continue
        except ValueError:
            split_worked = False
            print(f"Error - invalid parameter '{pair}'")
        try:
            if split_worked is False:
                continue
            if int(quantity) < 0:
                print(f"Error - invalid parameter '{quantity}'")
                continue
            inventory[item] = int(quantity)
        except ValueError as v:
            print(f"Quantity error for '{item}': {v}")
    return inventory


def inventory_analysis(inventory: dict[str, int]) -> None:
    total = sum(inventory.values())
    max_q = 0
    max_item = ""
    min_q = -1
    min_item = ""
    for item, quantity in inventory.items():
        if quantity > max_q:
            max_q = quantity
            max_item = item
        if min_q == -1:
            min_q = quantity
            min_item = item
        if min_q > quantity:
            min_q = quantity
            min_item = item
        print(f"Item {item} represents {round((quantity/total)*100, 1)}%")
    print(f"Item most abundant: {max_item} with quantity {max_q}")
    print(f"Item least abundant: {min_item} with quantity {min_q}")


def update_inventory(inventory: dict[str, int],
                     new_item: str) -> dict[str, int]:
    items_to_update: dict[str, int] = {}
    try:
        item, quantity = new_item.split(":")
    except ValueError:
        print(f"Error - invalid parameter '{new_item}'")
        return inventory
    try:
        if int(quantity) < 0:
            print(f"Error - invalid parameter '{quantity}'")
            return inventory
        items_to_update[item] = int(quantity)
        inventory.update(items_to_update)
    except ValueError as v:
        print(f"Quantity error for '{item}': {v}")
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inv = inventory_parser(sys.argv[1::])
    print(f"Got inventory: {inv}")
    print(f"Item list: {inv.keys()}")
    print(f"Total quantity of the {len(inv.keys())}",
          f"items: {sum(inv.values())}")
    inventory_analysis(inv)
    inv = update_inventory(inv, "wand: 1")
    inv = update_inventory(inv, "sword: value")
    print(f"Updated inventory: {inv}")
