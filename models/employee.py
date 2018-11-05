import sqlite3

class EmployeeModel:
    def __init__(self, name, email, department, phone):
        self.name = name
        self.email = email
        self.department = department
        self.phone = phone

    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM employees WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'employee': {'name': row[0], 'email': row[1], 'department': row[2], 'phone': row[3]}}
        
    def find_by_id(self, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM employees WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'employee': {'name': row[0], 'email': row[1], 'department': row[2], 'phone': row[3]}}

    def insert(self, employee):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO employees VALUES (?, ?, ?)"
        cursor.execute(query, (employee['name'], employee['email'], employee['department'], employee['phone']))
        connection.commit()
        connection.close()

    def update(self, employee):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE employees SET email=?, department=?, phone=? WHERE name=?"
        cursor.execute(query, (employee['email'], employee['department'], employee['phone'], employee['name']))
        connection.commit()
        connection.close()

        