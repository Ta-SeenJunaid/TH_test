from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api=Api(app)

client = MongoClient("mongodb://database:27017")
db = client.Th
collection = db["Collection"]

class Test(Resource):
    pass

if __name__=="__main__":
    app.run(host='0.0.0.0')
