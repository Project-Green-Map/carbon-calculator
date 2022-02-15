

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

'''
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
'''
