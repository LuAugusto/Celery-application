from flask import jsonify
from src.modules.locations.repo.locations_repo import locations_instance
import httpx
from src.modules.locations.exceptions.api_exceptions import RequestError

class GetLocations:
    def __init__(self, repository = locations_instance):
        self.__locations_instance = repository

    def execute(self):
        try:
            result = self.__locations_instance.get_locations()
            data = []
            for doc in result:
                data.append(doc)
            return jsonify(data)   
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 500:
                raise RequestError()
    
use_case = GetLocations()