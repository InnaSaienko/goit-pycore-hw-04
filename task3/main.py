import sys
from pathlib import Path
from draw_tree import draw_tree


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <directory_path>")
        return

    root_path = Path(sys.argv[1])
    if not root_path.exists() or not root_path.is_dir():
        print("Error: invalid path", file=sys.stderr)
        return
    draw_tree(root_path)

if __name__ == "__main__":
    main()