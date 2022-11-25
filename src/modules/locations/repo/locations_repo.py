from database.database import Database
from settings import variables

db = Database(variables.COLLECTION_FORECAST)

class LocationsRepo():
    def get_locations(self):
        return db.get_collection().aggregate([
            {'$match': {'days':{'$exists':True}}},
            {'$project': {'city': '$city_name', '_id': 0}},
            {'$sort': {'city': 1}}
        ])

    def get_when_sunrises_earlier(self, day: int):
        print(day)
        query = db.get_collection().aggregate([
            {'$match': {'days':{'$exists':True}}},
            {'$project': {'city': '$city_name', 'days': 1}},
            {'$project': {'city': 1, 'days': {'$filter': {'input':"$days", 'as':"day", 'cond': {'$eq': ["$$day.day", int(day)]} } } }},
            {'$addFields': {'days':{'$first':"$days"}}},
            {'$project': {'sunrise_ts': '$days.sunrise_ts', 'city': 1}},
            {'$sort': {'sunrise_ts': 1}},
            {'$limit': 10}
        ])
    
        return query
    
    def get_locations_with_less_wind(self):
        result = db.get_collection().aggregate([
            {'$match': {'days':{'$exists':True}}},
            {'$project': { 'city':'$city_name', 'values': {'$map':{'input': "$days", 'as': "day", 'in': {'$add': ["$$day.wind_gust_spd", 0]} }}  }},
            {'$project': {'city': 1, "average_speed_wind_5_days": {'$avg':"$values"}}},
            {'$sort': {'average_speed_wind_5_days': 1}},
            {'$limit': 10}
        ])
        
        return result

    def get_average_temperature(self, city: str):
        result = db.get_collection().aggregate([
            {'$match': {'city_name': city}},
            {'$project': { 'city':'$city_name',  'days': 1, 'max_temp': {'$map':{'input': "$days", 'as': "day", 'in': {'$add': ["$$day.max_temp", 0]} }}  }},
            {'$project': { 'city': 1, 'max_temp': 1, 'min_temp' : {'$map':{'input': "$days", 'as': "day", 'in': {'$add': ["$$day.min_temp", 0]} }}  }},
            {'$project': { 'city': '$city', "Média da temperatura máxima": {'$avg':"$max_temp"} , "Média da temperatura minima": {'$avg':"$min_temp"} } },
        ])
        
        return result
        

locations_instance = LocationsRepo()

