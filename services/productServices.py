import psycopg2


# get all product service
def get_all_products(cursor):
    try:
        # Execute query
        cursor.execute("SELECT * FROM product")
        # Retrieve query results
        records = cursor.fetchall()
        return records
    except psycopg2.Error as e:
        print("\nError retrieving products:", e)
        return []


# find a single product service
def find_single_product(cursor, product_id):
    try:
        # Execute query
        cursor.execute(f"SELECT * FROM product WHERE id = %s", (product_id,))
        # Retrieve query results
        records = cursor.fetchall()
        return records
    except psycopg2.Error as e:
        print("\nError retrieving product:", e)
        return []


# add product service
def add_product(cursor, product):
    if len(product) == 0:
        return

    try:
        # Construct the INSERT query
        insert_query = """
            INSERT INTO public.product (
                id, name, price, description, quantity, availability
            )
            VALUES (%s, %s, %s, %s, %s, %s);
        """

        # Execute the INSERT query with the product data
        cursor.execute(insert_query, (
            product['id'],
            product['name'],
            product['price'],
            product['description'],
            product['quantity'],
            product['availability']
        ))

        # Commit the changes to the database
        cursor.connection.commit()

        print("\nProduct added successfully!")

    except psycopg2.Error as e:
        # Handle database errors
        print("\nError adding product:", e)


# update product service
def update_product(cursor, product_id, product):
    if len(product) == 0:
        return

    is_exist = bool(find_single_product(cursor, product_id))

    if not is_exist:
        return print("\nProduct not found to update!")

    try:
        # Construct the UPDATE query
        update_query = """
            UPDATE public.product
            SET name = %s, price = %s, description = %s, quantity = %s, availability = %s
            WHERE id = %s;
        """

        # Execute the UPDATE query with the product data
        cursor.execute(update_query, (
            product['name'],
            product['price'],
            product['description'],
            product['quantity'],
            product['availability'],
            product_id
        ))

        # Commit the changes to the database
        cursor.connection.commit()

        print("\nProduct updated successfully!")

    except psycopg2.Error as e:
        print("\nError updating product:", e)


# delete product service
def delete_product(cursor, product_id):
    is_exist = bool(find_single_product(cursor, product_id))

    if not is_exist:
        return print("\nProduct not found to update!")

    try:
        # Execute the DELETE query
        cursor.execute(f"DELETE FROM product WHERE id = %s", (product_id,))

        # Commit the changes to the database
        cursor.connection.commit()

        print("\nProduct deleted successfully")
    except psycopg2.Error as e:
        print("\nError deleting product:", e)
