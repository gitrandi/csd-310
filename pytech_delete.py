import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.vtuzyr3.mongodb.net/?retryWrites=true&w=majority")
database = client["pytech"]
collection = database["students"]

# 1. Call the find() method and display the results to the terminal window.
cursor = collection.find()
print("All Documents:")
for document in cursor:
    print(document)

# 2. Call the insert_one() method and insert a new document into the collection with student_id 1010.
new_student = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "courses": ["Math", "English", "History"]
}
collection.insert_one(new_student)
print("\nDocument Inserted:", new_student)

# 3. Call the find_one() method and display the results to the terminal window.
found_student = collection.find_one({"student_id": 1010})
print("\nFound Document:")
print(found_student)

# 4. Call the delete_one() method by student_id 1010.
delete_result = collection.delete_one({"student_id": 1010})
print("\nDelete Result:")
print(delete_result.raw_result)  # Display the raw result of the delete operation

# 5. Call the find() method and display the results to the terminal window.
cursor_after_delete = collection.find()
print("\nDocuments after Deletion:")
for document in cursor_after_delete:
    print(document)

# Close the MongoDB connection
client.close()
