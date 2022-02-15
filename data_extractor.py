from openpyxl import load_workbook
import pandas

def extract_data(): 
    workbook = load_workbook(filename="CO2_data.xlsx")
    spreadsheet = workbook.active
    print(spreadsheet["D3"].value)

    dataframe = pandas.read_excel(io="C:/Users/Horea/Project_Green_Maps_CO2_CalculatorProject_Green_Maps_CO2_Calculator/carbon-calculator/CO2_data.xlsx", sheet_name="Sheet1")
    print(dataframe)


    
    dict={}
    for i in range(1,9,2):
        fuels = {}
        fuels["Diesel"] = dataframe.loc[i,"Diesel"]
        fuels["Petrol"] = dataframe.loc[i,"Petrol"]
        fuels["Hybrid"] = dataframe.loc[i,"Hybrid"]
        dict[dataframe.iloc[i,1]] = fuels
    
    print(dict)

extract_data()