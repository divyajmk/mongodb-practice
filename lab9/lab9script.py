#!/home/gitpod/.pyenv/shims/python3



from pymongo import MongoClient


connection_uri = "mongodb+srv://nmagee:20oRGqjmo88JOF0k@cluster0.pnxzwgz.mongodb.net/"
database = "yaq7fm"
collection = "UVAcourses"

# Use MongoDB Atlas connection
client = MongoClient(connection_uri)

# Switch to UVA computing ID database
db = client[database]

# Create a new collection
new_collection = db[collection]

# Insert at least 5 Documents 
new_collection.insert_many( [
   { "Department": "Computer Science Department", "Number of Classes": 100, "Class Size": 350, "Status": "Closed" },
   { "Department": "Data Science Department", "Number of Classes": 30, "Class Size": 50, "Status": "Open" },
   { "Department": "Applied Mathematics Department", "Number of Classes": 15, "Class Size": 60, "Status": "Open" },
   { "Department": "Economics Department", "Number of Classes": 50, "Class Size": 200, "Status": "Closed" },
   { "Department": "Psychology Department", "Number of Classes": 20, "Class Size": 150, "Status": "Open" },
   { "Department": "Biology Department", "Number of Classes": 80, "Class Size": 250, "Status": "Open" },
] )

# Find Documents (of exactly three)
open_classes = new_collection.find({"Status": "Open"}).limit(3)

# Display these three documents 
for c in open_classes:
    print(c)
