from data_extractor import extract_data
from json_reader import compute_route_consumption
import functions_framework

from step_by_step import SimpleStepByStep


class Vehicle_Info:
    model = "average"
    fuel = "unkown"


@functions_framework.http
def mr_carbon(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request_json:
        print("Processing request")
        routes = request_json["routes"]
        vehicle_info = request_json["vehicle_info"]

        sbs_calc = SimpleStepByStep()
        consumptions = sbs_calc.calculate(google_routes=routes, vehicle_info=vehicle_info, verbose=False)
        print(consumptions)
        return str(consumptions)
    else:
        return f'We have a problem - no json received'

"""
def main_json(json):
    extract_data()
    consumptions = [compute_route_consumption(route,vehicle_info) for route in routes]
    return str(consumptions)

def initialize_vehicle_info(json):
    vehicle_info = Vehicle_Info()
    ### MODEL
    if("brand" in json.keys() and "model" in json.keys()):
        vehicle_info.model = json["brand"] + ' ' + json['model']
    else:
        if("size" in json.keys()):
           vehicle_info.model = json["size"]
        
    ### FUEL
    if("fuel" in json.keys()):
        vehicle_info.fuel = json["fuel"] 
    
    return vehicle_info
"""