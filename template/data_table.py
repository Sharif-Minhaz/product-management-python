from tabulate import tabulate

headers = ['Product ID', 'Name', 'Price ($)', 'Description', 'Quantity', 'Availability']


def generate_data_table(data):
    # Truncate the description to a certain length (e.g., 50 characters)
    truncated_data = [(item[0], item[1], item[2], item[3][:50] + '...', item[4], item[5]) for item in data]
    table = tabulate(truncated_data, headers=headers, tablefmt="grid")

    table = f"\n{table}"

    print(table)
