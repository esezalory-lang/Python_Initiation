#!/bin/python3


class GardenError(Exception):
    default_error = "Unknown garden error"

    def __init__(self: "GardenError", message: str | None) -> None:
        if message is None:
            super().__init__(self.default_error)
        else:
            super().__init__(message)


class PlantError(GardenError):
    default_error = "Unknown plant error"


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'\n"
                         ".. ending tests and returning to main")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(test_status: bool) -> None:
    valid_tests = ["Tomato", "Lettuce", "Carrots"]
    invalid_tests = ["Tomato", "lettuce"]

    if test_status is True:
        try:
            print("Testing valid plants...")
            print("Opening watering system")
            for plant in valid_tests:
                water_plant(plant)
        except PlantError as p:
            print(f"Caught {PlantError.__name__}: {p}")
        finally:
            print("Closing watering system\n")
    else:
        try:
            print("Testing invalid plants...")
            print("Opening watering system")
            for plant in invalid_tests:
                water_plant(plant)
        except PlantError as p:
            print(f"Caught {PlantError.__name__}: {p}")
        finally:
            print("Closing watering system\n")


if __name__ == "__main__":

    print("=== Garden Watering System ===\n")
    test_watering_system(True)
    test_watering_system(False)
    print("Cleanup always happens, even with errors!")
