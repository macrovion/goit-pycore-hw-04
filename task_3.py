# створюємо нове віртуальне оточення
# python -m venv .venv

# активуємо нове оточення
# source venv/bin/activate

# інсталимо бібліотеку
# pip install colorama

# код скрипту:

import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path: Path, prefix: str = ''):
    try:
        entries = list(path.iterdir())
    except PermissionError:
        print(prefix + Fore.RED + '[Permission Denied]')
        return

    entries.sort(key=lambda e: (e.is_file(), e.name.lower()))

    for i, entry in enumerate(entries):
        connector = '┗' if i == len(entries) - 1 else '┣'
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + ' 📂' + entry.name + Style.RESET_ALL)
            new_prefix = prefix + ('  ' if i == len(entries) - 1 else '┃ ')
            print_directory_structure(entry, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + ' 📜' + entry.name + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + 'Usage: python hw03.py /path/to/directory')
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f'Error: Path \"{dir_path}\" does not exist.')
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f'Error: Path \"{dir_path}\" is not a directory.')
        sys.exit(1)

    print(Fore.BLUE + '📦' + dir_path.name + Style.RESET_ALL)
    print_directory_structure(dir_path)

if __name__ == '__main__':
    main()
