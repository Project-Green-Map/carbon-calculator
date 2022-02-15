from json_reader import extract_distances
    
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
        return main_json(request_json)
    else:
        return f'We have a problem - no json received'


def main_json(json):
    magic_constant_per_km = 3.5
    distances = extract_distances(json)
    distances = [d * magic_constant_per_km for d in distances]
    return str(distances)