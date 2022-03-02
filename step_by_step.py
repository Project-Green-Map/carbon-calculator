import string
from typing import List
from click import MissingParameter
from numpy import full_like, argmin

from speed_mul import * 
from get_co2e import read_db


# Interface for a step-by-step-caculator class
# process_vehicle_info and per_step interacts by manipuating the state of the class
class StepByStepInterface:
    def per_step(self, google_step) -> float:
        return 0.0

    def process_vehicle_info(self, vehicle_info):
        pass
    
    def calculate(self, google_routes, vehicle_info, verbose=True) -> float:
        self.process_vehicle_info(vehicle_info)

        # potential future optimisation:
        # legs = [r['legs'] for r in routes] # [[[R1L1] [R1L2]] []]
        # steps = [l['steps'] for r in legs for l in r] # [[[[R1L1S1][R1L1S2][R1L1S3]] [[][][]] ] []]
        
        carbon_by_route: List[float] = []

        for nr, r in enumerate(google_routes):
            legs = r['legs']
            carbon_by_leg = []
            for nl, l in enumerate(legs):
                steps = l['steps']
                carbon_by_step = [self.per_step(s) for s in steps]
                if verbose:
                    print(f"R{nr}L{nl}: {carbon_by_step}")
                carbon_by_leg.append(sum(carbon_by_step))
            if verbose:
                print(f"R{nr} {carbon_by_leg}")
            carbon_by_route.append(sum(carbon_by_leg))
        
        return carbon_by_route
            

class SimpleStepByStep(StepByStepInterface):
    def _reset_state(self):
        self.co2e_per_km: float = 170.0
    
    def __init__(self):
        self._reset_state()

    def per_step(self, google_step) -> float:
        # TODO: Detect transport type
        distance = google_step['distance']['value']
        time = google_step['duration']['value']
        mps = distance / time
        kmh = mps * 3.6
        
        return distance / 1000.0 * self.co2e_per_km * get_multiplier(kmh)

    def process_vehicle_info(self, vehicle_info):
        self._reset_state()

        if "brand" in vehicle_info.keys() and "model" in vehicle_info.keys():
            brand = vehicle_info["brand"].strip().upper()
            model = vehicle_info["model"].strip().upper()
            fuel  = vehicle_info["fuel"].strip().upper() if "fuel" in vehicle_info.keys() else "UNKNOWN"
            year  = vehicle_info["year"] if "year" in vehicle_info.keys() else 2022

            try:
                self.co2e_per_km: float = read_db(brand=brand, model=model, fuel=fuel, year=year)
                return
            except Exception as e:
                print("[Vehicle Info: ] Missing " + str(e))
        

        # TODO: Need to do fall back calculation here       
        return
            

        
        


        



    
    
