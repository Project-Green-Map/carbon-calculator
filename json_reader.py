from enum import Enum

from calculator import car_calculation, cycling_calculation, public_transport_calculation

class Travel_Mode(Enum):
    car = 1
    public_transport = 2
    cycling = 3
    walking = 4
    
def extract_distances(json):
    distances_km = []
    routes = json["routes"]
    for route in routes:
        distance_meters = 0
        legs = route["legs"]
        for leg in legs:
            distance_meters += leg["distance"]["value"]
        distances_km.append(distance_meters / 1000)
    return distances_km

def compute_route_consumption(route, vehicle_info):
    total_carbon = 0 
    distances = {Travel_Mode.car:0, Travel_Mode.public_transport: 0, Travel_Mode.cycling: 0, Travel_Mode.walking: 0}
    legs = route["legs"]
    for leg in legs:
        steps = leg["steps"]
        for step in steps:
            distance = step["distance"]["value"]/1000
            travel_mode = step["travel_mode"]
            if(travel_mode =="DRIVING"):
                distances[Travel_Mode.car] += distance
            elif(travel_mode == "TRANSIT"): ###??
                distances[Travel_Mode.public_transport] += distance
            elif(travel_mode == "CYCLING"):
                distances[Travel_Mode.cycling] += distance
            else:
                distances[Travel_Mode.walking] += distance

    total_carbon += car_calculation(distances[Travel_Mode.car], vehicle_info.model, vehicle_info.fuel)
    total_carbon += public_transport_calculation(distances[Travel_Mode.public_transport],"Railway")
    total_carbon += cycling_calculation(distances[Travel_Mode.cycling])
    return total_carbon

