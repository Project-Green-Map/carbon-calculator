from openpyxl import load_workbook
import pandas
all_data = {}

def extract_data(): 
    workbook = load_workbook(filename="CO2_data.xlsx")
    spreadsheet = workbook.active

    ### Extracting car data 
    car_dataframe = pandas.read_excel(io="CO2_data.xlsx", sheet_name="Cars")

    car = {}
    for i in range(1,9,2):
        fuels = {}
        fuels["Diesel"] = car_dataframe.loc[i,"Diesel"]
        fuels["Petrol"] = car_dataframe.loc[i,"Petrol"]
        fuels["Hybrid"] = car_dataframe.loc[i,"Hybrid"]
        car[car_dataframe.iloc[i,1]] = fuels
    all_data["car"] = car

    ### Extracting public transport data 
    public_transport_dataframe =  pandas.read_excel(io="CO2_data.xlsx", sheet_name="Public_transport")

   
    public_transport = {}
    for i in range (0,public_transport_dataframe.shape[0]):
        public_transport[public_transport_dataframe.iloc[i,0]] = public_transport_dataframe.iloc[i,1]
    all_data["public_transport"] = public_transport

    all_data["walinkg"] = 0
    all_data["cycling"] = 0.005
    print(all_data)

def get_car_value(car_type, fuel_type):
    return all_data["car"][car_type][fuel_type]

def get_public_transport_value(transport_type):
    return all_data["public_transport"][transport_type]

def get_cycling_value():
    return all_data["cycling"]
