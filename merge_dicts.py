import json

dict_paths = [
    "Make_dict_1.json",
    "Make_dict_2.json"
]
dictionaries=[]

for path in dict_paths:
    with open(path) as brand_dict_file:
        dictionaries.append(json.load(brand_dict_file))


result_dict = dictionaries[0]
for i in range(1, len(dictionaries)):
    for key, val in dictionaries[i].items():
        if key in result_dict:
            if val != result_dict[key]:
                print(f"found a conflict: key: {key}, val: {val},  val present: {result_dict[key]}")
        else:
            result_dict[key] = val

with open("Make_dict.json", "w") as outfile:
    json.dump(result_dict, outfile, indent=4, sort_keys=True)