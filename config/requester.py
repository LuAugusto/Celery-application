import requests
import json
from settings import variables
from database.database import Database
from config.errors import Errors

feed_database = Database(variables.COLLECTION_LOGS_ERROR)

class Requester():
    def __init__(self, url: str) -> None:
        self.url = url
    
    def make_url(self, city, country, days, key):
        url =  f'{self.url}?city={city}&country={country}&days={int(days)}&lang=pt&key={key}'
        return self.make_request(url)
    
    def make_request(self, url):
        request = requests.get(url)
        
        if request.status_code not in ['200', 200, '204', 204]:
            erro = Errors(request.status_code)
            feed_database.get_collection().insert_one({'status_code': request.status_code, 'error': erro})
            return
            
        if not(request.content):
            return []
        
        body = json.loads(request.content)
        return body