import sys
import typing


def read_file(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO = open(filename, "r")
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError, FileExistsError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        read_file(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
