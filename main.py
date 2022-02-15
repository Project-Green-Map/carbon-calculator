from distance_getter import calculation
from enum import Enum

class Transport_method(Enum):
    WALKING = 1
    CYCLING = 2
    CAR = 3
    PUBLIC_TRANSPORT = 4

class Data:
    def __init__(self, JSON_file):
        self.distance = 2
        self.type = Transport_method.CAR
        self.model = "DIESEL_TESLA"

    def consumption_perModel(self):  ### gets the model and returns the CO2 emissions per km
        if(self.model=="DIESEL_TESLA"):
            return 10.5
        return 7.5
    
    def compute_emmisions(self):
        return self.distance * self.consumption_perModel()

    

def main(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message') + "don't want this"
    elif request_json:
        # here we want to write stuff, request_json is just the dictionary representing the json
        if "distance" not in request_json:
            return "sorry, can't do a calculation"

        d = request_json["distance"]
        
        return str(calculation(d))
    else:
        return f'We have a problem'

    JSON_file = "example.JSON"
    new_data = Data(JSON_file)
    print(new_data.compute_emmisions())
    print()

main()
