import pymongo
import pprint

client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
ticket_db = client["ticket_db"]
# userlog = ticket_db["userlog"]
# userlog.insert_one({"name": "John", "role": "member", "status": "valid"})

pprint(client.list_database_names())
# print(ticket_db.list_collection_names())

# for db in userlog.find():
#     print(db["name"])
#     print(db)
# if "ticket_db" in client.list_database_names():
#     print("The database exists.")
