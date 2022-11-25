from src.modules.locations.use_cases.get_average_temperature.get_average_temperature import use_case

class GetAverageTemperatureController:
    def __init__(self, service = use_case):
        self.__service = service
        
    def execute(self, city):
        return self.__service.execute(city)

get_average_temperature_controller = GetAverageTemperatureController()