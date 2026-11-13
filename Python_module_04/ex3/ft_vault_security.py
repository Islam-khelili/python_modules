def secure_archive(
        file_name: str,
        mode: str = "r",
        content: str = "") -> tuple[bool, str]:
    try:
        if mode == 'r':
            with open(file_name, "r") as file:
                return (True, file.read())
        elif mode == 'w':
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))


"""
if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("filenotexisting", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("fragments.txt", "r"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("lasttest.txt", "w", "test"))
"""
