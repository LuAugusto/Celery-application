from src.modules.locations.use_cases.get_locations.get_locations import use_case

class GetLocationsController:
    def __init__(self, service = use_case ):
        self.__service = service
        
    def execute(self):
        return self.__service.execute()

get_locations_controller = GetLocationsController()