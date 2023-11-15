import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.vtuzyr3.mongodb.net/?retryWrites=true&w=majority")
database = client["pytech"]
collection = database["students"]

# 1. Call the find() method and output the documents to the terminal window.
cursor = collection.find()
for document in cursor:
    print(document)

# 2. Call the update_one method by student_id 1007 and update the last name.
query = {"student_id": 1007}
update = {"$set": {"last_name": "NewLastName"}}
collection.update_one(query, update)

# 3. Call the find_one method by student_id 1007 and output the document to the terminal window.
updated_document = collection.find_one({"student_id": 1007})
print("Updated Document:", updated_document)
