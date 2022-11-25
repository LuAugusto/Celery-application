from flask import jsonify
from src.modules.locations.repo.locations_repo import locations_instance
import httpx
from src.modules.locations.exceptions.api_exceptions import RequestError

class GetLocationsWithLessWind:
    def __init__(self, repository = locations_instance):
        self.__locations_instance = repository

    def execute(self):
        try:
            result = self.__locations_instance.get_locations_with_less_wind()
            data = []
            for doc in result:
                doc["average_speed_wind_5_days"] = round(doc["average_speed_wind_5_days"], 2)
                if doc["_id"]:
                    doc['_id'] = str(doc['_id'])
                    data.append(doc)
                else:
                    data.append(doc)
            return jsonify(data)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 500:
                raise RequestError()

use_case = GetLocationsWithLessWind()