from flask import Flask,jsonify,request
from pymongo import MongoClient
from datetime import datetime
import redis ,json


app=Flask(__name__)
red = redis.Redis(host="0.0.0.0",port=6379)

client = MongoClient("mongodb://localhost:27017")
db = client.sample
samples = db["samples"]


@app.route("/show/<name>",methods=["GET"])
def show(name):
    print("Check in Redis")
    val = red.get(name=name)

    if(val is None ):
        print("Calling from DataBase")
        data = samples.find({"name":name})
        mongo_data=[]
        for item in data:
            mongo_data.append({
                "msg": "Calling from Database",
                "name": item["name"],
                "price": item["price"],
                "time": str(item["time"])
            })
            red.set(item["name"],json.dumps({
                "msg": "Calling from Redis",
                "name": item["name"],
                "price": item["price"],
                "time": str(item["time"])
            }))
        return jsonify(mongo_data)
    else:
        print("Redis Data")
        #val = val.replace("b","")
        #print("Val value")
        val=val.decode("utf-8")
        #print(val)
        return val
        
    

@app.route("/show",methods=["GET"])
def show_all():
    data = samples.find({})
    #print(data)
    mongo_data=[]
    for item in data:
        #print(item)
        mongo_data.append({
            "_id": str(item["_id"]),
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
        "time": datetime.now()
    })

    ret={
        "Status": 200,
        "Msg": "Success added data"
    }

    return jsonify(ret)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)