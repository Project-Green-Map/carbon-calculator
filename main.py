from data_extractor import extract_data
from json_reader import compute_route_consumption

#import functions_framework

class Vehicle_Info:
    model = "average"
    fuel = "unkown"

'''
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
        # here we want to write stuff, request_json is just the dictionary representing the json
        return main_json(request_json)
    else:
        return f'We have a problem - no json received'
'''

def main_json(json):
    extract_data()
    routes = json["routes"]
    vehicle_info =  initialize_vehicle_info(json)
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


    
### Deprecated
'''
def compute(json):
    if(json["vechicle_type"]=="car"):
        ### MODEL
        if("brand" in json.keys() and "model" in json.keys()):
            model = json["brand"] + ' ' + json['model']
        else:
            if("size" in json.keys()):
                model = json["size"]
            else:
                model = "average"
        
        ### FUEL
        if("fuel" in json.keys()):
            fuel = json["fuel"] 
        else:
            fuel = "unknown"
        
        return car_calculation(extract_distances(json),model,fuel)

    elif(json["vehicle_type"]=="public_transport"):
        return 0
    elif(json["vehicle_type"]=="cycling"):
        return cycling_calculation(extract_distances(json))
    else:
        return 0; ### walking
'''