from data_extractor import extract_data
from json_reader import compute_route_consumption
import functions_framework
import time

from step_by_step import SimpleStepByStep

<<<<<<< HEAD
import functions_framework
=======
>>>>>>> 69dbd8cf476e1e32af47daec3cdb400742725360

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
        start = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
        print("========= Processing request =========")
        routes = request_json["routes"]
        vehicle_info = request_json["vehicle_info"] if "vehicle_info" in request_json.keys() else {}

        sbs_calc = SimpleStepByStep()
        consumptions = sbs_calc.calculate(google_routes=routes, vehicle_info=vehicle_info, verbose=False)
        print(consumptions)
        end = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
        elapse_ms = (end-start) * 1e-6
        print(f"===== End of request ({elapse_ms: .4f}ms) =====")
        print()
        return  str(consumptions)
    else:
<<<<<<< HEAD
        return f'We have a problem - no json received'

=======
        return  'We have a problem - no POST json received'
    
>>>>>>> 69dbd8cf476e1e32af47daec3cdb400742725360

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