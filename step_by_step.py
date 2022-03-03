from typing import List
from warnings import warn

from speed_mul import * 
from get_co2e import read_db
from get_fallback import read_fallback_values
from get_transit import get_bus_emission, get_rail_emission


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
        self.good_vehicle_info: bool = True
    
    def __init__(self):
        self._reset_state()

    def _per_step_driving(self, google_step) -> float:
        if not self.good_vehicle_info:
            warn("[Vehicle Info: ] Calculating driving carbon with no vehicle data, probably a horrible idea!")

        distance = google_step['distance']['value']
        time = google_step['duration']['value']
        mps = distance / time
        kmh = mps * 3.6
        
        return distance / 1000.0 * self.co2e_per_km * get_multiplier(kmh)


    def _per_step_transit(self, google_step) -> float:
        distance_km = google_step['distance']['value'] / 1000

        details = google_step['transit_details'] # this should exist, DirectionsTransitDetails 
        if "line" not in details.keys():
            warn("[Vehicle Info: transit] Skipped step: missing `line` in DirectionsTransitDetails")
            return 0.0
        
        line = details['line'] #DirectionsTransitLine
        if "vehicle" not in line.keys():
            warn("[Vehicle Info: transit] Skipped step: missing `vehicle` in DirectionsTransitLine")
            return 0.0
        
        vehicle = line['vehicle'] #DirectionsTransitVehicle 
        if vehicle['type'] in ['BUS', 'INTERCITY_BUS']:
            return get_bus_emission() * distance_km
        else:
            return get_rail_emission() * distance_km
    

    def per_step(self, google_step) -> float:
        if google_step["travel_mode"] == "DRIVING":
            return self._per_step_driving(google_step)
        elif google_step["travel_mode"] == "TRANSIT":
            return self._per_step_transit(google_step)
        else:
            return 0.0 # walking, cycling


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
        

        # Do fall back calculation here
        if "size" not in vehicle_info.keys():
            print("[Vehicle Info: ] Incomplete vehicle_info, using default value!")
            self.good_vehicle_info = False
            return
               
        size = vehicle_info["size"] if "size" in vehicle_info.keys() else ""
        fuel = vehicle_info["fuel"] if "fuel" in vehicle_info.keys() else ""
        print(f"[Vehicle Info: ] Fallback used: ({size}, {fuel})")
        self.co2e_per_km = read_fallback_values(size, fuel)
        

            

        
        


        



    
    
