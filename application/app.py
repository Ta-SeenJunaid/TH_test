from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from datetime import datetime


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
        collection.create_index("date", expireAfterSeconds= 60)
        collection.insert({
            "key" : key,
            "value" : value,
            "date" : datetime.utcnow()
        })

        retJson = {
            "status" : 200,
            "message" : "Successfully inserted!!!!!!!!"
        }

        return jsonify(retJson)


    def get(self, key=None):

        data =[]

        if key:
            d = collection.find_one({"key": key})
            if d:
                data.append({"key" : d["key"], "value": d["value"], "date": d["date"]})

                retJson = {
                    "status": 200,
                    "result" : data
                }

                return jsonify(retJson)

            else:
                retJson = {
                    "status" : 302,
                    "message" : "No data available!!!!!!!"
                }

                return jsonify(retJson)



        for d in collection.find():
            data.append({"key" : d["key"], "value": d["value"], "date": d["date"]})

        retJson = {
            "status" : 200,
            "result" : data
        }

        return jsonify(retJson)

    def patch(self, key):
        patchData = request.get_json()

        d = collection.find_one({"key": key})
        if not d:
            retJson = {
                "status" : 303,
                "message" : "Key unavailable!!!!!!!"
            }

            return jsonify(retJson)


        value = patchData["value"]

        collection.update({"key" : key
        },{
            "$set" : {
                "value" : value
            }
        })

        retJson = {
            "status" : 200,
            "message" : "Patch successfull!!!!!"
        }

        return jsonify(retJson)



api.add_resource(Test, '/values', '/values/<string:key>')


if __name__=="__main__":
    app.run(host='0.0.0.0')
