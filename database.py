import sqlite3


def initialize_db():
    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    availability TEXT,
    rating REAL,
    url TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, UNIQUE(name,url))""")
    conn.commit()
    conn.close()


def save_to_db(products):
    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()
    for product in products:
        cursor.execute(""" 
        INSERT INTO products (name, price, availability, rating, url) VALUES (?,?,?,?,?) 
        ON CONFLICT(name, url) DO UPDATE SET
        price = excluded.price,
        availability = excluded.availability,
        last_updated = CURRENT_TIMESTAMP""",
                       (product['name'], product['price'], product['availability'], product['rating'], product['url']))
    conn.commit()
    conn.close()



def get_all_products():
    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, availability, rating, url, last_updated FROM products")
    products = cursor.fetchall()
    conn.close()
    print(products)
    return products


def check_database_contents():
    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    print(rows)


def insert_sample_data():
    products = [
        {
            "name": "Asus AsusPro Adv",
            "price": 1139.54,
            "availability": "In Stock",
            "rating": 4.5,
            "url": "http://example.com/product1"
        },
        {
            "name": "Asus ROG Strix G",
            "price": 1101.83,
            "availability": "In Stock",
            "rating": 4.8,
            "url": "http://example.com/product2"
        },
        {
            "name": "Acer Aspire 3 A3",
            "price": 494.71,
            "availability": "Not available",
            "rating": 4.0,
            "url": "http://example.com/product3"
        }
    ]

    save_to_db(products)  # Save sample products to the database


if __name__ == "__main__":
    initialize_db()  # Initialize the database# Clear existing products
    insert_sample_data()  # Insert sample data into the database
    check_database_contents()  # Check and print database contents
