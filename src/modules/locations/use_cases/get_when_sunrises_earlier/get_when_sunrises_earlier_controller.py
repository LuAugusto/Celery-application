from src.modules.locations.use_cases.get_when_sunrises_earlier.get_when_sunrises_earlier import use_case

class GetWhenSunrisesEarlierController:
    def __init__(self, service = use_case):
        self.__service = service
        
    def execute(self, day: int):
        return self.__service.execute(day)

get_when_sunrises_earlier_controller = GetWhenSunrisesEarlierController()