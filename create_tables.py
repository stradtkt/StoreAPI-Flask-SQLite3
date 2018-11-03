import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name text, location text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name text, price real, description text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name text, email text, department text, phone text)"
cursor.execute(create_table)
connection.commit()
connection.close()