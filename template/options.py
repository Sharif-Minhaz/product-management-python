from colorama import init, Fore, Style

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)

options = ("View all products", "Search for a product", "Add a product", "Update a product", "Delete a product", "Exit")


def generate_all_options():
    print("\nAll available options:")
    for index, option in enumerate(options, start=1):
        formatted_option = f"{Fore.GREEN}{index}){Style.RESET_ALL} {option}"
        print(formatted_option)
