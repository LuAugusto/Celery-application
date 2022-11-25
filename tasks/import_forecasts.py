from settings import variables
from config.requester import Requester
from database.database import Database
from datetime import datetime
from pytz import timezone


requester = Requester(variables.WEATHER_API_URL)

class ImportForecasts():
    def import_forecasts(self, city: str):
        feed_database = Database(variables.COLLECTION_FORECAST)

        data = self.fetch_data(city)
        
        body = self.validate_data(data)
        
        location = feed_database.get_collection().find_one({'city_name': city})
        if not(location):
            if body:
                feed_database.insert_one_data(body)
            else:
                feed_database.insert_one_data({'city_name': city, 'data': 0})
        elif location:
            if body:
                feed_database.get_collection().update_one({'city_name': city}, {'$set': body})
            
    def fetch_data(self, city):
        return requester.make_url(city, country=variables.COUNTRY, days=variables.DAYS, key=variables.KEY)
    
    def validate_data(self, body: dict):
        if not(body):
            return []
        final_data = []
        
        for dados in body.get('data'):
            data = {}
            actual_day = datetime.strptime(dados.get('datetime'), '%Y-%m-%d')
            data.update({'app_max_temp': dados.get('app_max_temp')})
            data.update({'app_max_temp': dados.get('app_max_temp')})
            data.update({'max_temp': dados.get('max_temp')})
            data.update({'min_temp': dados.get('min_temp')})
            data.update({'temp': dados.get('temp')})
            data.update({'wind_dir': dados.get('wind_dir')})
            data.update({'wind_cdir_full': dados.get('wind_cdir_full')})
            data.update({'wind_gust_spd': dados.get('wind_gust_spd')})
            data.update({'datetime': actual_day})
            data.update({'day': actual_day.day})
            data.update({'sunrise_ts':datetime.fromtimestamp(float(dados.get('sunrise_ts')), tz = timezone("Europe/Lisbon"))})
            data.update({'sunset_ts':datetime.fromtimestamp(float(dados.get('sunset_ts')), tz = timezone("Europe/Lisbon"))})

            final_data.append(data)
            
        del body['data']
        
        body.update({'days':final_data})
        
        return body