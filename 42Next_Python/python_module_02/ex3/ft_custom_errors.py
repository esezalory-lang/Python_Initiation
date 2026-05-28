#!/bin/python3

ERROR_1 = "The tomato plant is wilting!"
ERROR_2 = "Not enough water in the tank!"


class GardenError(Exception):
    default_error = "Unknown garden error"

    def __init__(self: "GardenError", message: str | None) -> None:
        if message is None:
            super().__init__(self.default_error)
        else:
            super().__init__(message)


class PlantError(GardenError):
    default_error = "Unknown plant error"


class WaterError(GardenError):
    default_error = "Unknown water error"


def custom_error(water_status: str) -> None:
    if water_status == "dry":
        raise PlantError(ERROR_1)
    else:
        raise WaterError(ERROR_2)


def test_pnw_errors(garden_status: bool, water_status: str) -> None:
    if garden_status is True:
        try:
            custom_error(water_status)
        except PlantError as p:
            print(f"Caught {PlantError.__name__}: {p}\n")
        except WaterError as w:
            print(f"Caught {WaterError.__name__}: {w}\n")
    else:
        try:
            custom_error(water_status)
        except GardenError as p:
            print(f"Caught {GardenError.__name__}: {p}")


def print_message(msg_idx: int) -> None:
    if msg_idx > 2:
        return
    error_messages = [
        "Testing PlantError..",
        "Testing WaterError...",
        "Testing catching all garden errors..."
    ]
    print(error_messages[msg_idx])


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    statuses = {
        True: ["dry", "wet"],
        False: ["dry", "wet"]
    }

    msg_idx = 0
    for garden_status, water_statuses in statuses.items():
        for status in water_statuses:
            print_message(msg_idx)
            test_pnw_errors(garden_status, status)
            msg_idx += 1

    print("\nAll error types tested work correctly!")
