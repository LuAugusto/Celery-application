from settings import variables
from config.requester import Requester
from database.feed_database import FeedDatabase

requester = Requester(variables.WEATHER_API_URL)

class ImportForecasts():
    def import_forecasts(self, city: str):
        feed_database = FeedDatabase(variables.COLLECTION_FORECAST)

        body = self.fetch_data(city)
        
        location = feed_database.get_collection().find_one({'city_name': city})
        if not(location):
            if body:
                feed_database.insert_one_data(body)
            else:
                feed_database.insert_one_data({'city_name': city, 'data': 0})
        elif location or location.get('data') == 0:
            if body:
                feed_database.get_collection().update_one({'city_name': city}, {'$set': body})
            
    def fetch_data(self, city):
        return requester.make_url(city, country=variables.COUNTRY, days=variables.DAYS, key=variables.KEY)