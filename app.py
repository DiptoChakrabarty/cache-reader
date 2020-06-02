from flask import Flask
from pymongo import MongoClient


app=Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client.cloud
clouds = db["clouds"]



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)