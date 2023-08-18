from colorama import init, Fore, Style

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)


def generate_heading(heading_text):
    border = f"{Fore.BLUE}{'=' * 37}{Style.RESET_ALL}"
    heading = f"{Fore.CYAN}{Style.BRIGHT}{heading_text}{Style.RESET_ALL}"

    print(border)
    print(heading.center(50))
    print(border)
