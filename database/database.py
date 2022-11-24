from database.mongo import client
from settings import variables

class Database():
    def __init__(self, collection: str = variables.COLLECTION_FORECAST) -> None:
        self.collection = collection
    
    def get_collection(self):
        return client.get_collection(self.collection)
        
    def insert_one_data(self, data):
        collection = self.get_collection()
        collection.insert_one(data)
        return

    def check_database(self):
        forecast = client.get_collection(variables.COLLECTION_FORECAST).find()
        location = client.get_collection(variables.COLLECTION_LOCATION).find()
        if not(forecast) or not(location):
            return None
        else:
            return True