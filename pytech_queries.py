import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]

# Find all documents in the collection
all_students = db.students.find({})

# Display all documents
for student in all_students:
    print(student)
