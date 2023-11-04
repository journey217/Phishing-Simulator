from base64 import b64encode
from hashlib import sha256

from pymongo import MongoClient
import bcrypt

mongo_client = MongoClient("mongo")
db = mongo_client["Client"]
accounts_collection = db["Accounts"]


def add_to_DB(email, password):
    enc_pass = hash_pass(password)
    account_insert = {"email": email, "password": enc_pass}
    accounts_collection.insert_one(account_insert)
    return


def hash_pass(password):
    salt = bcrypt.gensalt()
    encoded = encode_pass(password)
    hashed_password = bcrypt.hashpw(encoded, salt)
    return hashed_password


def encode_pass(password):
    return b64encode(sha256(password.encode()).digest())

