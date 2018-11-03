import sqlite3

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM products WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'product': {'name': row[0], 'price': row[1], 'description': row[2]}}
        
    def find_by_id(self, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM products WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'product': {'name': row[0], 'price': row[1], 'description': row[2]}}

    def insert(self, product):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO products VALUES (?, ?, ?)"
        cursor.execute(query, (product['name'], product['price'], product['description']))
        connection.commit()
        connection.close()

    def update(self, product):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE products SET price=?, description=? WHERE name=?"
        cursor.execute(query, (product['price'], product['description'], product['name']))
        connection.commit()
        connection.close()