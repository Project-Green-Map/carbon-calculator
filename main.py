from data_extractor import extract_data
from json_reader import compute_route_consumption
import functions_framework
import time

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
        start = time.time_ns()
        print("========= Processing request =========")
        routes = request_json["routes"]
        vehicle_info = request_json["vehicle_info"] if "vehicle_info" in request_json.keys() else {}

        sbs_calc = SimpleStepByStep()
        consumptions = sbs_calc.calculate(google_routes=routes, vehicle_info=vehicle_info, verbose=False)
        print(consumptions)
        end = time.time_ns()
        elapse_ms = (end-start) * 1e-6
        print(f"===== End of request ({elapse_ms: .4f}ms) =====")
        print()
        return  str(consumptions)
    else:
        return  'We have a problem - no POST json received'
    