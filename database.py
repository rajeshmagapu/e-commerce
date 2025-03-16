import sqlite3

def get_db_connection():
    conn = sqlite3.connect('store.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, image TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, cart TEXT)")

    # Insert static products
    cursor.execute("DELETE FROM products")  # Clear old data
    products = [
        ("Dove Soap", 2.99, "static/images/dove_soap.jpg"),
        ("Head & Shoulders Shampoo", 5.49, "static/images/head_shoulders.jpg"),
        ("Colgate Toothpaste", 3.29, "static/images/colgate.jpg"),
        ("Nivea Body Lotion", 7.99, "static/images/nivea_lotion.jpg"),
        ("Dettol Handwash", 4.99, "static/images/dettol.jpg")
    ]
    cursor.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)

    conn.commit()
    conn.close()

init_db()
