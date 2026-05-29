#!/bin/python3

import math


def distance_to_center(set_1: tuple[float, ...] = (0.0, 0.0, 0.0),
                       set_2: tuple[float, ...] = (0.0, 0.0, 0.0)
                       ) -> float:
    x = (set_2[0] - set_1[0])**2
    y = (set_2[1] - set_1[1])**2
    z = (set_2[2] - set_1[2])**2
    distance = math.sqrt(x + y + z)
    return distance


def get_player_pos() -> tuple[float, ...]:
    while True:
        print("Enter new coordinates as floats in format 'x,y,z': ", end="")
        inputs = input().split(",")
        n_inputs = 0
        for i in inputs:
            n_inputs += 1
        if n_inputs != 3:
            print("Invalid Syntax")
            continue
        clean_inputs = []
        has_bad_input = False
        for i in inputs:
            try:
                clean_inputs += [float(i)]
            except ValueError as v:
                has_bad_input = True
                print(f"Error on parameter '{i}': {v}")
        if has_bad_input is True:
            continue
        coordinates = tuple(clean_inputs)
        return coordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    set_1 = get_player_pos()
    print(f"Got a first tuple: {set_1}")
    print(f"It includes: X={set_1[0]}, Y={set_1[1]}, Z={set_1[2]}")
    print(f"Distance to center: {round(distance_to_center(set_1), 4)}\n")
    print("Get a second set of coordinates")
    set_2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          f"{round(distance_to_center(set_1, set_2), 4)}")
