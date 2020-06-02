from flask import Flask,jsonify,request
from pymongo import MongoClient
from datetime import datetime


app=Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client.sample
samples = db["samples"]


@app.route("/show",methods=["GET"])
def show_all():
    data = samples.find({})
    mongo_data=[]
    for item in data:
        mongo_data.append({
            "name": item["name"],
            "price": item["price"],
            "time": item["time"]
        })
    return jsonify(mongo_data)

@app.route("/add",methods=["POST"])
def add_data():
    data = request.get_json()
    samples.insert({
        "name": data["name"],
        "price": data["price"],
        "time": datetime.datetime.now()
    })

    ret={
        "Status": 200,
        "Msg": "Success added data"
    }

    return jsonify(ret)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)