import sys
import typing


def read_file(filename: str) -> str:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO = open(filename, "r")
        content: str = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        sys.stdout.write(f"File '{filename}' closed.\n")
        return content
    except (FileNotFoundError, PermissionError, FileExistsError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return ""


def add_hash_at_end(text: str) -> str:
    result: str = ""
    lines: list = text.splitlines()
    for line in lines:
        result += line + "#\n"
    return result


def save_file(filename: str, content: str) -> None:
    try:
        file: typing.IO = open(filename, "w")
        file.write(content)
        file.close()
        sys.stdout.write(f"Data saved in file '{filename}'.\n")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")


def ft_archive_creation(file_name: str) -> None:
    content: str = read_file(file_name)
    if content != "":
        print("Transform data:")
        print("---")
        hash_text: str = add_hash_at_end(content)
        print(hash_text, end="")
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()  # flush to terminal
        filename: str = sys.stdin.readline().strip()
        if filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{filename}'")
            save_file(filename, hash_text)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_archive_creation(sys.argv[1])
    else:
        print("Usage: ft_archive_creation.py <file>")
