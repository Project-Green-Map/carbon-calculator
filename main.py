from calculator import calculation
from enum import Enum
    

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
    if request_json:
        # here we want to write stuff, request_json is just the dictionary representing the json

        if "distance" not in request_json:
            return "sorry, can't do a calculation"

        #d = request_json["distance"]
        
        return 2 #str(calculation(d))
    else:
        return f'We have a problem - no json received'

