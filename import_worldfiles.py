import os, json, sys
from pymongo import MongoClient
curr_dir = os.getcwd()
curr_dir = os.fsencode(curr_dir)

connection_string = sys.argv[1] # First parameter



def setupMongoConnection(connection_string):
    m_client = MongoClient(connection_string)
    db = m_client["world_information"] # Hard coded value for project 
    Collection = db["countries"] # Using the hard coded collections
    return Collection
db_collection = setupMongoConnection(connection_string)
for i, (path, subdirs, files) in enumerate(os.walk(curr_dir)):
    for file in files:
        file = os.fsdecode(file)
        file_size = (len(file))
        # Check if file is json and adheres to the country file format i.e (**.json)
        if (file.endswith('.json') and (file_size==7)):
            file_path = "{}/{}".format(os.fsdecode(path), file)
            with open(file_path) as j_f:
                file_data = json.load(j_f)
            if isinstance(file_data, list):
                db_collection.insert_many(file_data)
            else:
                db_collection.insert_one(file_data)
print("All Factbook files have been added to the MongoDB database.") 
