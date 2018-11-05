import sqlite3
from flask import Flask, request
from flask_restful import Resource, reqparse
from models.employee import EmployeeModel

class Employee(Resource):
    def get(name):
        employee = EmployeeModel.find_by_name(name)
        if employee:
            return employee
        return {'message': 'Employee not found'}
    def get(id):
        employee = EmployeeModel.find_by_id(id)
        if employee:
            return employee
        return {'message': 'Employee not found'}

    def post(name):
        if EmployeeModel.find_by_name(name):
            return {'message': "A employee with the name of '{}' already exists".format(name)}
        data = Employee.parser.parse_args()
        employee = {'name': name, 'email': email, 'department': department, 'phone': phone}
        try:
            EmployeeModel.insert(employee)
        except:
            return {'message': 'An error has occurred adding the employee'}, 500
        return employee, 201

    def delete(self, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM employees WHERE id=?"
        cursor.execute(query, (id,))
        connection.commit()
        connection.close()
        return {'message': 'Employee deleted'}

    def put(name):
        data = Employee.parser.parse_args()
        employee = EmployeeModel.find_by_name(name)
        updated_employee = {'name': name, 'email': email, 'department': department, 'phone': phone}
        if employee is None:
            try:
                EmployeeModel.insert(updated_employee)
            except:
                return {'message': 'An error occurred adding the employee.'}
        else:
            try:
                EmployeeModel.update(updated_employee)
            except:
                return {'message': 'An error has occurred updating the employee'}
        return updated_employee

    
class EmployeeList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM employees"
        result = cursor.execute(query)
        employees = []
        for row in result:
            employees.append({'name': row[0], 'email': row[1], 'department': row[2], 'phone': row[3]})

        connection.close()
        return {'employees': employees}