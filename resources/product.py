import sqlite3
from flask import Flask
from flask_restful import Resource, reqparse
from ..models.product import ProductModel

class Product(Resource):
    def get(name):
        pass
    def get(id):
        pass

    def post(name):
        pass

    def delete(self, id):
        pass

    def put(name):
        pass

    
class ProductList(Resource):
    def get(self):
        pass