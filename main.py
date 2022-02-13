import distance_getter
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

    

def main():
    JSON_file = "example.JSON"
    new_data = Data(JSON_file)
    print(new_data.compute_emmisions())
    print()

main()
