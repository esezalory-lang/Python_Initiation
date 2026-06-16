#!/bin/python3


def secure_archive(filename: str, action: str,
                   content: str = "") -> tuple[bool, str]:
    open_worked = True
    read_info = ""
    if action == 'r':
        try:
            with open(filename, action) as input:
                read_info = input.read()
        except Exception as e:
            open_worked = False
            indication = (False, f"{e}")
    else:
        try:
            with open(filename, action) as input:
                input.write(content)
        except Exception as e:
            open_worked = False
            indication = (False, f"{e}")
    if open_worked is False:
        result = indication
    else:
        if action == 'r':
            indication = (True, read_info)
        else:
            indication = (True, 'Content successfully written to file')
        result = indication
    return result


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure archive' to read from a nonexistent file:")
    result = secure_archive("nonexistent.txt", 'r', "")
    print(result)
    print()

    print("Using 'secure archive' to read from a inaccessible file:")
    result = secure_archive("inaccessible.txt", 'r', "")
    print(result)
    print()

    print("Using 'secure archive' to read from a regular file:")
    result = secure_archive("reading.txt", 'r', "")
    print(result)
    print()

    print("Using 'secure archive' to write previous content to a new file:")
    result = secure_archive("writing.txt", 'w', "new content to write")
    print(result)
