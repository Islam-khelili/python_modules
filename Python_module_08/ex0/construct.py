import sys
import os
import site


def detect_venv() -> bool:
    return sys.prefix != sys.base_prefix


def venv_info() -> None:
    print(f"""\n\nMATRIX STATUS: Welcome to the construct\n
Current Python: {sys.executable}
Virtual Environment: {os.path.basename(sys.prefix)}
Environment Path: {sys.prefix}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:\n{site.getsitepackages()[0]}
""")


def instruction_create_venv() -> None:
    print(f"""\n\n MATRIX STATUS: You're still plugged in

Current Python: {sys.executable}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows\n
Then run this program again.""")


if __name__ == "__main__":
    if detect_venv():
        venv_info()
    else:
        instruction_create_venv()
