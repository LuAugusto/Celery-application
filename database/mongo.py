from pymongo import MongoClient
from settings import variables

def connect_database():
    return MongoClient(variables.MONGO_DB_URL).db


client = connect_database()