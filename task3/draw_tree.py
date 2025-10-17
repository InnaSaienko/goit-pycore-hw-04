import os
from pathlib import Path
from colorama import Fore, Style

FILE_COLOR = Fore.GREEN
DIR_COLOR = Fore.BLUE
RESET = Style.RESET_ALL

# Graphics
VERTICAL_LINE = '│   '
INNER_ENTRY = '├── '
LAST_ENTRY = '└── '


def draw_tree(path: Path, depth: int = 1):
    print(f"{DIR_COLOR}{path.name}{os.sep}{RESET}", end="")

    try:
        entries = list(path.iterdir())
    except OSError:
        print(f" [Could not read directory contents]")
        return

    print("")

    last_idx = len(entries) - 1

    for i, entry in enumerate(entries):
        connector = LAST_ENTRY if i == last_idx else INNER_ENTRY
        print(f"{VERTICAL_LINE * (depth - 1)}{connector}", end="")

        if entry.is_dir():
            draw_tree(entry, depth + 1)
        else:
            print(f"{FILE_COLOR}{entry.name}{RESET}")
