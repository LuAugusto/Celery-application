from flask import Response
from app import server
from src.modules.locations.use_cases.get_locations.get_locations_controller import get_locations_controller
from src.modules.locations.use_cases.get_when_sunrises_earlier.get_when_sunrises_earlier_controller import get_when_sunrises_earlier_controller
from src.modules.locations.use_cases.get_locations_with_less_wind.get_locations_with_less_wind_controller import get_locations_with_less_wind_controller
from src.modules.locations.use_cases.get_average_temperature.get_average_temperature_controller import get_average_temperature_controller

@server.app.route('/')
def get_locations():
    return get_locations_controller.execute()

@server.app.route('/locations/sunrises/earlier/<day>')
def get_when_sunrises_earlier(day):
    return get_when_sunrises_earlier_controller.execute(day)

@server.app.route('/locations/wind')
def get_locations_with_less_wind():
    return get_locations_with_less_wind_controller.execute()

@server.app.route('/locations/average/temperature/<city>')
def get_averag_temperature(city):
    return get_average_temperature_controller.execute(city)


server.run()