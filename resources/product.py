from flask import Flask, request
from flask_restful import Resource, reqparse
from models.product import ProductModel

class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
            type=float,
            required=True,
            help="This field cannot be left blank"
    )
    def get(self, name):
        product = self.find_by_name(name)
        if product:
            return product.json()
        return {'message': 'Product not found.'}

    def get(self, id):
        product = self.find_by_id(id)
        if product:
            return product.json()
        return {'message': 'Product not found.'}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An product with the name '{}' already exists.".format(name)}
        data = Product.parser.parse_args()
        product = ProductModel(name, **data)
        try:
            product.save_to_db()
        except:
            return {'message': 'An error has occurred inserting the product'}, 500
        return product.json(), 201

    def delete(self, id):
        product = self.find_by_id(id)
        if product:
            product.delete_from_db()
        return {'message': 'product deleted'}

    def put(self, name):
        data = Product.parser.parse_args()
        product = ProductModel.find_by_name(name)
        if product is None:
            product = ProductModel(name, **data)
        else:
            product.price = data['price']
            product.save_to_db()
        return product.json()

    
class ProductList(Resource):
    def get(self):
        return {'products': list(map(lambda x: x.json(), ProductModel.query.all()))}