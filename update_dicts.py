import json

dict_paths = [
    "Make_dict_1.json",
    "Make_dict_2.json"
]

dict_master_path = "Make_dict.json" #current version

dictionaries=[]

for path in dict_paths:
    with open(path) as brand_dict_file:
        dictionaries.append(json.load(brand_dict_file))

dict_master = {}
with open(dict_master_path) as brand_dict_file:
    dict_master = json.load(brand_dict_file)


for i in range(len(dictionaries)):
    for key, val in dict_master.items():
        if key in dictionaries[i]:
            if val != dictionaries[i][key]:
                print(f"found a conflict: key: {key}, val: {val},  val2: {dictionaries[i][key]}")
                dictionaries[i][key] = val #update
        
for i in range(len(dictionaries)):
    with open(dict_paths[i], "w") as outfile:
       json.dump(dictionaries[i], outfile, indent=4, sort_keys=True)