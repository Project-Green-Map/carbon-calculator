import pandas
all_data = {}

class Defaults:
    public_transport_default = 1
    average_car_default = 2

def extract_data(): 
    ### Extracting car data 
    car_dataframe = pandas.read_excel(io="CO2_data.xlsx", sheet_name="Cars")

    car = {}
    for i in range(1,9,2):
        fuels = {}
        fuels["diesel"] = car_dataframe.loc[i,"diesel"]
        fuels["petrol"] = car_dataframe.loc[i,"petrol"]
        fuels["hybrid"] = car_dataframe.loc[i,"hybrid"]
        fuels["unknow"] = car_dataframe.loc[i,"unknown"]
        car[car_dataframe.iloc[i,1]] = fuels
    all_data["car"] = car

    ### Extracting public transport data 
    public_transport_dataframe =  pandas.read_excel(io="CO2_data.xlsx", sheet_name="Public_transport")

   
    public_transport = {}
    for i in range (0,public_transport_dataframe.shape[0]):
        public_transport[public_transport_dataframe.iloc[i,0]] = public_transport_dataframe.iloc[i,1]
    all_data["public_transport"] = public_transport

    all_data["walinkg"] = 0
    all_data["cycling"] = 0.000001
    print(all_data)

def get_car_value(car_type, fuel_type):
    if(car_type in all_data["car"]):
        if(fuel_type in all_data["car"][car_type]):
            return all_data["car"][car_type][fuel_type]
        else:
            print("DANGER")
            return all_data["car"][car_type]["diesel"]
    else:
        return -1

def get_public_transport_value(transport_type):
    return all_data["public_transport"][transport_type]

def get_cycling_value():
    return all_data["cycling"]
