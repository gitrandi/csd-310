import pymongo
from pymongo import MongoCLient
client = MongoClient("mongodb+srv://admin:admin@cluster0.vtuzyr3.mongodb.net/?retryWrites=true&w=majority")
new_students = [
    {
        "student_id": "1007",
        "first_name": "Alice",
        "last_name": "Johnson",
        "age": 20,
        "email": "alice@example.com"
    },
    {
        "student_id": "1008",
        "first_name": "Bob",
        "last_name": "Smith",
        "age": 22,
        "email": "bob@example.com"
    },
    {
        "student_id": "1009",
        "first_name": "Charlie",
        "last_name": "Brown",
        "age": 21,
        "email": "charlie@example.com"
    }
]

# Insert each document and display the returned student_id
for new_student in new_students:
    new_student_id = db.students.insert_one(new_student).inserted_id
    print(f"Inserted document with student_id: {new_student_id}")

