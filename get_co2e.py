from pathlib import Path
from json import load
from numpy import argmin

folder_path = Path("carbon_db") #using Path to make sure it is compatible among different OS.

def main(brand, model, fuel, year):
    co2e_g_per_km = 0
    file_path = folder_path / (brand + ".json")
    if not file_path.is_file():
        raise Exception(f"brand: {brand} was not recognised")
    
    file = open(file_path, "r")
    brand_dict = load(file)
    
    if model not in brand_dict:
        raise Exception(f"model: {model} was not recognised")

    if fuel not in brand_dict[model]:
        old_fuel = fuel
        if "PETROL" in brand_dict[model]:
            fuel = "PETROL"
        elif "DIESEL" in brand_dict[model]:
            fuel = "DIESEL"
        else:
            fuel = list(brand_dict[model].keys())[0] #we just take what is available
        print(f"[Vehicle Info: /{brand}/{model}/{fuel}] Subs: {fuel} <- {old_fuel}")

    available_years = list(brand_dict[model][fuel].keys())
    if year not in available_years:
        _minarg = argmin([abs(int(y)-year) for y in available_years])
        closest_year = available_years[_minarg]
        print(f"[Vehicle Info: /{brand}/{model}/{fuel}] Subs {closest_year} <- {year}")
        co2e_g_per_km = brand_dict[model][fuel][closest_year]
    else:
        co2e_g_per_km = brand_dict[model][fuel][year]

    print("[Vehicle Info: /{brand}/{model}/{fuel}/{year}] Emission/km: {co2e_g_per_km}")
    return co2e_g_per_km

#random test
print(main('AUDI', 'A1', 'Not recognised fuel', 2010))
