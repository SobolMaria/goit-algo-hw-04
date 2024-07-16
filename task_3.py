from pathlib import Path
from colorama import Fore, Back, Style


def print_dir_content(current_dir=Path('.'), shift=0):
    extensions_colors_png = {'.png': Fore.YELLOW + Back.BLUE}
    extensions_colors_bmp = {'.bmp': Fore.BLUE + Back.RED}
    extensions_colors_jpg = {'.jpg': Fore.RED + Back.YELLOW}

    for path in current_dir.iterdir():
        if path.is_dir():
            print(' ' * shift + f'- {path.name}')
            print_dir_content(path, shift + 3)
        else:
            match path.suffix:
                case '.png':
                    styles = extensions_colors_png[path.suffix]
                    print(' ' * shift + styles + path.name + Style.RESET_ALL)
                case '.bmp':
                    styles = extensions_colors_bmp[path.suffix]
                    print(' ' * shift + styles + path.name + Style.RESET_ALL)
                case '.jpg':
                    styles = extensions_colors_jpg[path.suffix]
                    print(' ' * shift + styles + path.name + Style.RESET_ALL)
                case _:
                    print(' ' * shift + path.name + Style.RESET_ALL)

print_dir_content()