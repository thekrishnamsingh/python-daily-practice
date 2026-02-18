def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print("Invalid integer input")
        return None


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found")
        return None


if __name__ == "__main__":
    print(safe_int_conversion("123"))
    print(safe_int_conversion("abc"))

    print(read_file("sample.txt"))
    print(read_file("nonexistent.txt"))
