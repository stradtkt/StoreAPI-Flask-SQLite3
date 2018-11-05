from flask import Flask
from flask_restful import Api
from resources.product import Product, ProductList
from models.product import ProductModel
from resources.employee import Employee, EmployeeList
from models.employee import EmployeeModel
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "d;fkjdslfhda ckudhck.sadch. dkczhd.c gzd ch "
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Product, '/products/<string:name>')
api.add_resource(Product, '/products/<int:id>')
api.add_resource(ProductList, '/products')
api.add_resource(EmployeeList, '/employees')
api.add_resource(Employee, '/employees/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)