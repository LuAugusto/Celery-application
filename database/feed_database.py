from database.mongo import client

class FeedDatabase():
    def __init__(self, collection: str) -> None:
        self.collection = collection
    
    def get_collection(self):
        return client.get_collection(self.collection)
        
    def insert_one_data(self, data):
        collection = self.get_collection()
        collection.insert_one(data)
        return

