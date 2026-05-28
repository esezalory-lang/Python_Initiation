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
    statuses = {
        True: ["Tomato", "Lettuce", "Carrots"],
        False: ["Tomato", "lettuce"]
    }
    try:
        for system_status, plant_names in statuses.items():
            for plant in plant_names:
                if system_status is True and plant == "Tomato":
                    print("Testing valid plants...")
                    print("Opening watering system")
                elif system_status is False and plant == "Tomato":
                    print("Testing invalid plants...")
                    print("Opening watering system")
                water_plant(plant)
            print()
    except PlantError as p:
        print(f"Caught {PlantError.__name__}: {p}")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":

    print("=== Garden Watering System ===\n")
    test_watering_system(True)
    test_watering_system(False)
    print("Cleanup always happens, even with errors!")
