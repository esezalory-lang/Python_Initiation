#!/bin/python3

def input_temperature(temp_str: str) -> int:
    print(f"Temperature is now {int(temp_str)}°C\n")
    return int(temp_str)


def test_temperature() -> None:
    valid_temp = "25"
    invalid_temp = "abc"
    try:
        print("Input data is '25'")
        input_temperature(valid_temp)
        print("Input data is 'abc'")
        input_temperature(invalid_temp)
        print("Input data is None ")
        test_temperature()
    except ValueError as v:
        print(f"Caught input_temperature error: {v}\n")
    except TypeError as t:
        print(f"Caught input_temperature error: {t}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
