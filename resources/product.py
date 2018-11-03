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