import string
from typing import List
from numpy import full_like, argmin, absolute

from main import Vehicle_Info
from speed_mul import * 


# Interface for a step-by-step-caculator class
# process_vehicle_info and per_step interacts by manipuating the state of the class
class StepByStepInterface:
    def per_step(self, google_step) -> float:
        return 0.0

    def process_vehicle_info(self, vehicle_info):
        pass
    
    def calculate(self, google_routes, vehicle_info) -> float:
        self.process_vehicle_info(vehicle_info)
        routes = google_route['routes']

        # potential future optimisation:
        # legs = [r['legs'] for r in routes] # [[[R1L1] [R1L2]] []]
        # steps = [l['steps'] for r in legs for l in r] # [[[[R1L1S1][R1L1S2][R1L1S3]] [[][][]] ] []]
        
        carbon_by_route: List[float] = []

        for nr, r in enumerate(routes):
            legs = r['legs']
            carbon_by_leg = []
            for nl, l in enumerate(legs):
                steps = l['step']
                carbon_by_step = [self.per_step(s) for s in steps]
                print(f"R{nr}L{nl}: {carbon_by_step}")
                carbon_by_leg.append(carbon_by_step)
            print(f"R{nr} {carbon_by_leg}")
            carbon_by_route.append(sum(carbon_by_leg))
        
        return carbon_by_route
            

class SimpleStepByStep(StepByStepInterface):
    def _reset_state(self):
        self.co2e_per_km: float = 170.0
    
    def __init__(self, dataframe):
        self._reset_state()
        self._df = dataframe

    def per_step(self, google_step) -> float:
        distance = google_step['']['value']
        time = google_step['duration']['value']
        mps = distance / time
        kmh = mps * 3.6
        
        return distance / 1000.0 * self.co2e_per_km * get_multiplier(kmh)

    def process_vehicle_info(self, vehicle_info):
        self._reset_state()
        brand = string.strip(string.upper(vehicle_info.brand))
        model = string.strip(string.upper(vehicle_info.model))
        fuel  = string.strip(string.upper(vehicle_info.fuel))
        year  = vehicle_info.year

        if brand not in self._df['Make'].unique():
            print(f"[Vehicle Info: /] Unable to find brand {brand}")
            return
        
        brand_df = self._df.loc[self._df['Make']==brand]
        
        if model not in brand_df['Model'].unique():
            print(f"[Vehicle Info: /{brand}] Unable to find model {model}")
            return
        
        model_df = brand_df.loc[brand_df['Mode']==model]

        if fuel not in model_df['Fuel'].unique():
            print(f"[Vehicle Info: /{brand}/{model}] Unable to find fuel {fuel}")
            return
        
        fuel_df = model_df.loc[model_df['Fuel']==fuel]


        available_years = list(fuel_df['year'].unique())
        if year not in available_years:
            _minarg = argmin([abs(y-year) for y in available_years])
            closest_year = available_years[_minarg]
            print("[Vehicle Info: /{brand}/{model}/{fuel}] Subs {closest_year} <- {year}")
            self.co2e_per_km = fuel_df.loc[fuel_df['year']==closest_year]['Emission'].iloc[0]
        else:
            self.co2e_per_km = fuel_df.loc[fuel_df['year']==year]['Emission'].iloc[0]
        
        print("[Vehicle Info: /{brand}/{model}/{fuel}/{year}] Emission/km: {self.co2e_per_km}")
        


        



    
    
