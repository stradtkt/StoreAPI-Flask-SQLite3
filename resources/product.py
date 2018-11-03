import sqlite3
from flask import Flask, request
from flask_restful import Resource, reqparse
from models.product import ProductModel

class Product(Resource):
    def get(name):
        product = ProductModel.find_by_name(name)
        if product:
            return product
        return {'message': 'Product not found'}
    def get(id):
        product = ProductModel.find_by_id(id)
        if product:
            return product
        return {'message': 'Product not found'}

    def post(name):
        if ProductModel.find_by_name(name):
            return {'message': "A product with the name of '{}' already exists".format(name)}
        data = Product.parser.parse_args()
        product = {'name': name, 'price': price, 'description': description}
        try:
            ProductModel.insert(product)
        except:
            return {'message': 'An error has occurred adding the product'}, 500
        return product, 201

    def delete(self, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM products WHERE id=?"
        cursor.execute(query, (id,))
        connection.commit()
        connection.close()
        return {'message': 'Product deleted'}

    def put(name):
        data = Product.parser.parse_args()
        product = ProductModel.find_by_name(name)
        updated_product = {'name': name, 'price': price, 'description': description}
        if product is None:
            try:
                ProductModel.insert(updated_product)
            except:
                return {'message': 'An error occurred adding the product.'}
        else:
            try:
                ProductModel.update(updated_product)
            except:
                return {'message': 'An error has occurred updating the product'}
        return updated_product

    
class ProductList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM products"
        result = cursor.execute(query)
        products = []
        for row in result:
            products.append({'name': row[0], 'price': row[1], 'description': row[2]})

        connection.close()
        return {'products': products}