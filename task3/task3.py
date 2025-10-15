from pathlib import Path

from colorama import Fore, Style

FILE_COLOR = Fore.GREEN
DIR_COLOR = Fore.BLUE
RESET = Style.RESET_ALL

# Symbols
VERT = '│ '
BRANCH = '├── '
LAST = '└── '
SPACE = '    '

def draw_tree(path: Path, prefix: str = ""):
    # try:
    #     files = list(path.iterdir())
    # except PermissionError:
    #     print(prefix + "[Permission denied]")
    #     return

    files = list(path.iterdir())
    try:
        for index, el in enumerate(files):
            is_last_element = index == len(files) - 1
            connector = LAST if is_last_element else BRANCH

            if el.is_dir():
                print(prefix + connector + f"{DIR_COLOR}{el.name}{RESET}/")
                extension = SPACE if is_last_element else VERT
                draw_tree(el, prefix + extension)
            else:
                print(prefix + connector + f"{FILE_COLOR}{el.name}{RESET}")


    except PermissionError:
        print(f"Invalid path to directory")
        return
