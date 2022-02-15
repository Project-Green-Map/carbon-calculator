from main import main_json
import json

def test1():
    f = open('test1.json')
    json1 = json.load(f)
    carbons = main_json(json1)
    print(carbons)
    
test1()