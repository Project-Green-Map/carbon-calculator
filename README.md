Calculation of CO2e for given set of routes through a HTTP request. Contains all data needed for carbon calculation. 

```
├── carbon_db                 # JSON files for each brand
├── processing_data           # Processes, Cleans, Prettifies EU db
├── test_cases                # contains JSONs of test cases 
├── carbon_db                 # JSON files for each car brand
├── calculator.py             # deprecated
├── car_defaults.json         # JSON for default car models
├── data_extractor.py         # deprecated: extract co2e data for simple cases
├── frontend_data.json        # deprecated data for frontend
├── get_co2e.py               # Gets co2 equivalent from carbon_db
├── get_fallback.py           # Default co2e if missing car specification
├── get_transit.py            # Gets co2e for transit option
├── json_reader.py            # [deprecated]: gets co2e for each route
├── main.py                   # Responds to http request, returns co2es
├── requirements.txt          # function dependencies
├── speed_mul.py              # Calculate CO2e based on speed
├── step_by_step.py           # Calculate step-by-step CO2e
├── tests.py                  # some tests
└── README.md     
```
