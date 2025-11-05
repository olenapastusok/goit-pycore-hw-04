import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def directory_visualization (path: Path, prefix: str = " "):

    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f'{prefix}{Fore.BLUE + item.name + "/"}')
                directory_visualization(item, prefix + "     ")
            else:
                print(f'{prefix}{Fore.GREEN+item.name}')
    except PermissionError:
        print(Fore.RED + "You do not have permission to directory" + str(path))
    except FileNotFoundError:
        print(Fore.RED + "File is not found" + str(path))


if len(sys.argv) != 2:
    print("Usage: python3 visualization.py <directory_path>")

root_path = Path(sys.argv[1])
print(Fore.YELLOW + "Directory structure: \n")
directory_visualization(root_path)
