from helpers.generate_unique_id import generate_product_id

from colorama import init, Fore, Style

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)


def str_to_bool(s):
    return s.lower() == "true"


# collect data from user
def collect_product_input():
    try:
        new_product = {
            'id': generate_product_id(),
            'name': input("Enter product name: "),
            'price': float(input("Enter product price: ")),
            'description': input("Enter product description: "),
            'quantity': int(input("Enter product quantity: ")),
            'availability': str_to_bool(input("Provide availability: "))
        }
        return new_product
    except ValueError:
        print(f"{Fore.RED}Invalid value provided.{Style.RESET_ALL}")
        return {}
