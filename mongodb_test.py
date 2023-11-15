import pymongo
from pymongo import MongoCLient
client = MongoClient("mongodb+srv://admin:admin@cluster0.vtuzyr3.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db ["students"]
print (db.list_collection_names)