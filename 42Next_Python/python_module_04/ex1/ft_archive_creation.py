#!/bin/python3

import sys
# import typing


if __name__ == "__main__":
    open_error = False
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        old_filename = sys.argv[1]
        try:
            file1 = open(old_filename, "r")
        except Exception as e:
            open_error = True
            print(f"Error opening file '{old_filename}': {e}")
        if open_error is False:
            print("---\n")
            old_content = file1.read()
            print(old_content)
            print("---")
            try:
                file1.close()
            except Exception as e:
                print(f"Error closing file '{file1}': {e}")
            print(f"File '{old_filename}' closed.\n")
        print("Transform data:")
        print("---\n")
        for line in old_content.split("\n"):
            line += "#"
            print(line)
        print("\n---")
        print("Enter new file name (or empty): ", end="")
        new_filename = input()
        if new_filename == "":
            print("Not saving data.")
        else:
            try:
                file2 = open(new_filename, "w")
            except Exception as e:
                open_error = True
                print(f"Error opening file '{new_filename}': {e}")
            if open_error is False:
                for old_line in old_content.split("\n"):
                    file2.write(old_line + "#\n")
            try:
                file2.close()
            except Exception as e:
                print(f"Error closing file '{file2}': {e}")
            print(f"Saving data to '{new_filename}'")
            print(f"Data saved in file '{new_filename}'.")
