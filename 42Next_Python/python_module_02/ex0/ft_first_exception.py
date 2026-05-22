#!/bin/python3

def input_temperature(temp_str: str) -> int:
    print(f"Temperature is now {int(temp_str)}°C\n")
    return int(temp_str)


def test_temperature(test_cases: str):
    input_temperature(test_cases)


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    valid_temp = "25"
    invalid_temp = "abc"

    try:
        print("Input data is '25'")
        test_temperature(valid_temp)
        print("Input data is 'abc'")
        test_temperature(invalid_temp)
        print("Input data is None ")
        test_temperature()
    except ValueError as v:
        print(f"Caught input_temperature error: {v}")
    except TypeError as t:
        print(f"Caught input_temperature error: {t}")
    print()
    print("All tests completed - program didn't crash!")
