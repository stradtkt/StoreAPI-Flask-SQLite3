from flask import Flask
from flask_restful import Api
import sqlite3
import create_tables
app = Flask(__name__)
api = Api(app)


api.add_resource(Product, '/products/<string:name>')
api.add_resource(Product, '/products/<int:id>')
api.add_resource(Product, '/products')
api.add_resource(Employee, '/employees')
api.add_resource(Employee, '/employees/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)