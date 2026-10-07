def secure_archieve(
        filename: str,
        action: str = "read",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename) as file:
                data = file.read()
            return (True, data)

        if action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        return (False, "Invalid actions")

    except Exception as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archieve' to read from a nonexistent file:")
    result = secure_archieve("/not/existing/file")
    print(f"{result}\n")

    print("Using 'secure_archieve' to read from an inaccessible file:")
    result = secure_archieve("/etc/shadow")
    print(f"{result}\n")

    print("Using 'secure_archieve' to read from a regular file:")
    result = secure_archieve("ancient_fragment.txt")
    print(f"{result}\n")

    print("Using 'secure_archieve' to write previous content to a new file:")
    if result[0]:
        result = secure_archieve("new_fragment.txt", "write", result[1])
    print(f"{result}\n")

# not needed but i just want to test
    print("Invalid action test")
    result = secure_archieve("idk", "test")
    print(result)


if __name__ == "__main__":
    main()
