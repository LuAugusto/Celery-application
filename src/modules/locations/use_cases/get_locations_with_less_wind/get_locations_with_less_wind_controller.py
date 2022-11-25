from src.modules.locations.use_cases.get_locations_with_less_wind.get_locations_with_less_wind import use_case

class GetLocationsWithLessWindController:
    def __init__(self, service = use_case):
        self.__service = service
        
    def execute(self):
        return self.__service.execute()

get_locations_with_less_wind_controller = GetLocationsWithLessWindController()