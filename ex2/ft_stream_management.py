import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_acient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archieves Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO = open(filename)
        content = file.read()

        print("---")
        print(content, end="")
        print("---")

        file.close()
        print(f"File '{filename}' closed.")

    except Exception as error:
        print(
                f"[STDERR] Error opening file '{filename}':"
                f"{error}", file=sys.stderr)
        return

# this is where the new stuff is added
    print("Transform data:")

    new_content = ""
    for char in content:
        if char == '\n':
            new_content += "#\n"
        else:
            new_content += char

    print("---")
    print(new_content, end="")
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename == "":
        print("Not saving data")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        new_file: typing.IO = open(new_filename, "w")
        new_file.write(new_content)
        new_file.close()

        print(f"Data saved in file '{new_filename}'")

    except Exception as error:
        print(
                f"[STDERR]Error saving file '{new_filename}:"
                f"{error}", file=sys.stderr
                )
        print("Data not saved.")


if __name__ == "__main__":
    main()
