import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute(" DROP TABLE IF EXISTS Products")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    i = 1
    # ЗАПОЛНЯЕМ 10-Ю ЗАПИСЯМИ
    for i in range(1, 4):
        cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
            (f"Продукт {i}", f"Описание {i}", f"{i*100}"))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    product = cursor.fetchall()
    connection.commit()
    connection.close()
    return product





