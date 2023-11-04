from pymongo import MongoClient
import bcrypt

mongo_client = MongoClient("mongo")
db = mongo_client["Client"]
accounts_collection = db["Accounts"]


def add_to_DB(email, password):
    enc_pass = generate_hashed_pass(password)
    account_insert = {"email": email, "password": enc_pass}
    accounts_collection.insert_one(account_insert)
    return


def generate_hashed_pass(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
