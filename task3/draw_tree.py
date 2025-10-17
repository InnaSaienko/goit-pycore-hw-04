import os
from pathlib import Path
from colorama import Fore, Style

FILE_COLOR = Fore.GREEN
DIR_COLOR = Fore.BLUE
RESET = Style.RESET_ALL

# Symbols
VERT = '│   '
BRANCH = '├── '
LAST = '└── '
SPACE = '    '

def draw_tree(path: Path, depth: int = 0):
    print(f"{DIR_COLOR}{path.name}{os.sep}{RESET}")
    try:
        entries = list(path.iterdir())
    except PermissionError:
        print(f"{VERT}[Permission Denied]")
        return

    for i, entry in enumerate(entries):
        print(f"{SPACE * depth}", end="")
        if entry.is_dir():
            draw_tree(entry, depth+1)
        else:
            print(f"{FILE_COLOR}{entry.name}{RESET}")



