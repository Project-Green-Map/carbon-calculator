from pathlib import Path
import json

folder_path = Path("carbon_db")

data = json.load(open(folder_path / "_Transit.json"))

def get_bus_emission():
    return data['BUS']

def get_rail_emission():
    return data['RAIL']