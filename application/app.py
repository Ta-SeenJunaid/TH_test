from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api=Api(app)

client = MongoClient("mongodb://database:27017")
db = client.Th
collection = db["Collection"]

class Test(Resource):
    def post(self):
        postedData = request.get_json()

        if "key" not in postedData or "value" not in postedData:
            retJson = {
                "status" : 301,
                "message" : "Missing key or value!!!!!!!"
            }

            return jsonify(retJson)

        key = postedData["key"]
        value = postedData["value"]

        collection.insert({
            "key" : key,
            "value" : value
        })

        retJson = {
            "status" : 200,
            "message" : "Successfully inserted!!!!!!!!"
        }

        return jsonify(retJson)


    def get(self):

        data =[]

        for d in collection.find():
            data.append({"key" : d["key"], "value": d["value"]})

        retJson = {
            "status" : 200,
            "result" : data
        }

        return jsonify(retJson)



api.add_resource(Test, '/values')


if __name__=="__main__":
    app.run(host='0.0.0.0')
