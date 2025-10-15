import sys
from pathlib import Path
from task3 import draw_tree

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
        return

    root_path_str = sys.argv[1]
    root_path = Path(root_path_str)
    if not root_path.exists() or not root_path.is_dir():
        print('Error: invalid path')
        return

    print(root_path.name + "/")
    draw_tree(root_path)

if __name__ == "__main__":
    main()