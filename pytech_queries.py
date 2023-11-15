import pymongo
from pymongo import MongoCLient
client = MongoClient("mongodb+srv://admin:admin@cluster0.vtuzyr3.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]

# Find all documents in the collection
all_students = db.students.find({})

# Display all documents
for student in all_students:
    print(student)
