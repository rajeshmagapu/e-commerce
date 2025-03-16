import sqlite3

def get_db_connection():
    conn = sqlite3.connect('store.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return products

def create_order(cart):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (cart) VALUES (?)", (str(cart),))
    order_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return order_id

def init_db():
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    conn.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, cart TEXT)")
    conn.commit()
    conn.close()

init_db()
