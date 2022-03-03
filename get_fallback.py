from pathlib import Path
import json

folder_path = Path("carbon_db") #using Path to make sure it is compatible among different OS.

def read_fallback_values(size: str, fuel: str):
    data = json.load(open(folder_path / "_Fallback.json"))

    if size.upper() not in data.keys():
        size = "AVERAGE"
    
    size_data = data[size.upper()]
    if fuel.upper() not in size_data.keys():
        fuel = "UNKNOWN"
    
    return size_data[fuel.upper()]
