from pymongo import MongoClient

mongo_client = MongoClient("mongo")
db = mongo_client["Client"]
accounts_collection = db["Accounts"]


def add_to_DB(email):
    account_insert = {"email": email}
    accounts_collection.insert_one(account_insert)
    return

