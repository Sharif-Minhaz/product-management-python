import psycopg2

conn = cur = None

try:
    # Connect to your PostgreSQL DB
    conn = psycopg2.connect("dbname=productsDB user=postgres password=admin123")
    print("Database connected successfully...")
    # Open a cursor to perform database operations
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Connection or database error:", e)
