# import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pymongo
from datetime import datetime, tzinfo, timezone
import requests
import json

# st.set_page_config(layout="wide")
import time
# st.title("Data Dashboard")
# st.markdown("**________________________________________________________________________________________________________________________________________________________________________________**")
# st.header(f"Platforms")



# Sample data
# @st.cache_resource(ttl=1800)
def dataload():
    # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=1"
    # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    # response = requests.request("GET", url, headers=headers)
    # print(response.text)
    # data1= json.loads(response.text)
    # print("\n\n\nStatus code::::",response.status_code)

    # # while response.status_code == 502:
    # #     response = requests.request("GET", url, headers=headers)
    # #     print("\n\n\nStatus code::::",response.status_code)
    # #     data1= json.loads(response.text)
        
    # print("Data 1 day: ",data1['data'])
    
    
    # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=7"
    # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    # response = requests.request("GET", url, headers=headers)
    # data7= json.loads(response.text)
    # print("\n\n\nStatus code::::",response.status_code)

    # # while response.status_code == 502:
    # #     response = requests.request("GET", url, headers=headers)
    # #     print("\n\n\nStatus code::::",response.status_code)
    # #     data7= json.loads(response.text)
        
    # print("Data 7 days: ",data7['data'])
    
    # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
    # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    # response = requests.request("GET", url, headers=headers)
    # data15= json.loads(response.text)
    # print("\n\n\nStatus code::::",response.status_code)

    # # while response.status_code == 502:
    # #     response = requests.request("GET", url, headers=headers)
    # #     print("\n\n\nStatus code::::",response.status_code)
    # #     data15= json.loads(response.text)
        
    # print("Data 15 days: ",data15['data'])
    
    # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
    # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    # response = requests.request("GET", url, headers=headers)
    # data30= json.loads(response.text)
    # print("\n\n\nStatus code::::",response.status_code)

    # # while response.status_code == 502:
    # #     response = requests.request("GET", url, headers=headers)
    # #     print("\n\n\nStatus code::::",response.status_code)
    # #     data30= json.loads(response.text)
        
    # print("Data 30 days: ",data30['data'])
    
    
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
    headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    response = requests.request("GET", url, headers=headers)
    data_lifetime= json.loads(response.text)
    print("\n\n\nStatus code::::",response.status_code)

    # while response.status_code == 502:
    #     response = requests.request("GET", url, headers=headers)
    #     print("\n\n\nStatus code::::",response.status_code)
    #     data_lifetime= json.loads(response.text)
        
    print("Data lifetime: ",data_lifetime['data'])
    
    return data_lifetime['data']

start_time= time.time()

data_lifetime= dataload()

print('\n\nTime taken by API: ',start_time-time.time())


# Data lifetime:  {'count': {'totalCount': 151818, 'activeCount': 70178, 'facebook': 990, 'activeFacebook': 990, 'gumtree': 14083, 'activeGumtree': 7643, 'autoTrader': 53653, 'activeAutoTrader': 33872, 'motors': 1350, 'activeMotors': 1274, 'heyCars': 2500, 'activeHeyCars': 1917, 'aiCars': 156, 'activeAiCars': 76}, 'active': {'priceMin': 100, 'priceMax': 799950, 'engineSizeInLiterMin': 0, 'engineSizeInLiterMax': 6.8, 'yearMin': 1936, 'yearMax': 2024, 'milageMin': 0, 'milageMax': 910000, 'distinctMakeCount': 88, 'distinctModelCount': 1042, 'topLargestInventoryMake': {'ABARTH': 152, 'ALFA ROMEO': 177, 'ALPINE': 10, 'ASTON MARTIN': 137, 'AUDI': 5525, 'AUSTIN': 2, 'Abarth': 4, 'BENTLEY': 207, 'BMW': 5172, 'BRISTOL': 1, 'BYD': 2, 'CADILLAC': 1, 'CATERHAM': 4, 'CHEVROLET': 116, 'CHRYSLER': 44, 'CITROEN': 1628, 'CUPRA': 150, 'DACIA': 447, 'DAEWOO': 2, 'DAIHATSU': 24, 'DAIMLER': 4, 'DODGE': 12, 'DS': 1, 'DS AUTOMOBILES': 111, 'FERRARI': 86, 'FIAT': 1269, 'FISKER': 1, 'FORD': 7235, 'GENESIS': 14, 'GWM ORA': 3, 'HONDA': 1479, 'HUMMER': 1, 'HYUNDAI': 2007, 'INEOS': 15, 'INFINITI': 28, 'ISUZU': 48, 'IVECO': 1, 'JAGUAR': 1061, 'JEEP': 244, 'KGM': 7, 'KIA': 1967, 'LAMBORGHINI': 47, 'LANCIA': 1, 'LAND ROVER': 3708, 'LEVC': 2, 'LEXUS': 122, 'LEXUS RX': 1, 'LONDON TAXIS INTERNATIONAL': 3, 'LOTUS': 46, 'LTI': 2, 'MASERATI': 95, 'MAZDA': 986, 'MAZDA 3': 1, 'MCLAREN': 23, 'MERCEDES-BENZ': 4764, 'MG': 332, 'MG MOTOR UK': 1, 'MG ZS': 2, 'MINI': 1621, 'MITSUBISHI': 428, 'MORGAN': 8, 'NISSAN': 3567, 'NOBLE': 1, 'OPEL': 1, 'OTHER': 18, 'PERODUA': 1, 'PEUGEOT': 2462, 'POLESTAR': 25, 'PORSCHE': 951, 'RENAULT': 1644, 'ROLLS-ROYCE': 58, 'ROVER': 52, 'SAAB': 67, 'SEAT': 1364, 'SKODA': 1834, 'SMART': 183, 'SSANGYONG': 153, 'SUBARU': 244, 'SUZUKI': 641, 'TESLA': 186, 'TOYOTA': 2723, 'TOYOTA, ALPHARD': 1, 'TRIUMPH': 3, 'TVR': 4, 'VAUXHALL': 4706, 'VOLKSWAGEN': 6059, 'VOLKSWAGEN CRAFTER': 1, 'VOLVO': 1636}, 'topLargestInventoryFuelType': {'Bi Fuel': 20, 'Diesel': 25026, 'Diesel Hybrid': 259, 'Diesel Plug-In Hybrid': 28, 'Electric': 2563, 'Flex': 3, 'Gas': 1, 'Gas Bi Fuel': 2, 'Hybrid': 731, 'Hybrid - Diesel/Electric': 2, 'Hybrid - Petrol/Electric': 117, 'Hybrid Electric': 503, 'Not Supplied': 24, 'Other': 31, 'Petrol': 37456, 'Petrol Hybrid': 2253, 'Petrol Plug-In Hybrid': 1148, 'Petrol/Gas': 1, 'Plug-In Hybrid': 5}}, 'checkerActivity': {'deactivatedCount': 151818, 'deactivatedCountFacebook': 990, 'deactivatedCountGumtree': 14083, 'deactivatedCountAutoTrader': 53653, 'deactivatedCountMotors': 1350, 'deactivatedCountHeyCars': 2500, 'deactivatedCountHeyAiCars': 156}}
# Data lifetime:  {'count': {'totalCount': 151117, 'activeCount': 71305, 'facebook': 913, 'activeFacebook': 913, 'gumtree': 13968, 'activeGumtree': 7839, 'autoTrader': 53267, 'activeAutoTrader': 34976, 'motors': 1278, 'activeMotors': 1214, 'heyCars': 2449, 'activeHeyCars': 1881, 'aiCars': 156, 'activeAiCars': 76}, 'active': {'priceMin': 100, 'priceMax': 799950, 'engineSizeInLiterMin': 0, 'engineSizeInLiterMax': 6.8, 'yearMin': 1936, 'yearMax': 2024, 'milageMin': 0, 'milageMax': 910000, 'distinctMakeCount': 87, 'distinctModelCount': 1034, 'topLargestInventoryMake': {'ABARTH': 153, 'ALFA ROMEO': 178, 'ALPINE': 10, 'ASTON MARTIN': 138, 'AUDI': 5585, 'AUSTIN': 2, 'Abarth': 4, 'BENTLEY': 209, 'BMW': 5242, 'BRISTOL': 1, 'BYD': 2, 'CADILLAC': 1, 'CATERHAM': 4, 'CHEVROLET': 118, 'CHRYSLER': 43, 'CITROEN': 1650, 'CUPRA': 151, 'DACIA': 453, 'DAEWOO': 2, 'DAIHATSU': 25, 'DAIMLER': 4, 'DODGE': 12, 'DS': 1, 'DS AUTOMOBILES': 110, 'FERRARI': 86, 'FIAT': 1292, 'FISKER': 1, 'FORD': 7362, 'GENESIS': 13, 'GWM ORA': 3, 'HONDA': 1503, 'HUMMER': 1, 'HYUNDAI': 2053, 'INEOS': 15, 'INFINITI': 29, 'ISUZU': 51, 'IVECO': 1, 'JAGUAR': 1100, 'JEEP': 243, 'KGM': 8, 'KIA': 2002, 'LAMBORGHINI': 46, 'LANCIA': 1, 'LAND ROVER': 3773, 'LEVC': 2, 'LEXUS': 124, 'LEXUS RX': 1, 'LONDON TAXIS INTERNATIONAL': 3, 'LOTUS': 47, 'LTI': 2, 'MASERATI': 96, 'MAZDA': 1006, 'MAZDA 3': 1, 'MCLAREN': 22, 'MERCEDES-BENZ': 4837, 'MG': 338, 'MG ZS': 2, 'MINI': 1653, 'MITSUBISHI': 438, 'MORGAN': 8, 'NISSAN': 3617, 'NOBLE': 1, 'OPEL': 1, 'OTHER': 18, 'PERODUA': 1, 'PEUGEOT': 2517, 'POLESTAR': 26, 'PORSCHE': 960, 'RENAULT': 1675, 'ROLLS-ROYCE': 58, 'ROVER': 54, 'SAAB': 70, 'SEAT': 1377, 'SKODA': 1860, 'SMART': 188, 'SSANGYONG': 155, 'SUBARU': 246, 'SUZUKI': 647, 'TESLA': 189, 'TOYOTA': 2749, 'TOYOTA, ALPHARD': 1, 'TRIUMPH': 3, 'TVR': 4, 'VAUXHALL': 4810, 'VOLKSWAGEN': 6156, 'VOLKSWAGEN CRAFTER': 1, 'VOLVO': 1660}, 'topLargestInventoryFuelType': {'Bi Fuel': 20, 'Diesel': 25460, 'Diesel Hybrid': 269, 'Diesel Plug-In Hybrid': 30, 'Electric': 2592, 'Flex': 3, 'Gas': 1, 'Gas Bi Fuel': 2, 'Hybrid': 720, 'Hybrid - Diesel/Electric': 2, 'Hybrid - Petrol/Electric': 113, 'Hybrid Electric': 495, 'Not Supplied': 25, 'Other': 30, 'Petrol': 38070, 'Petrol Hybrid': 2283, 'Petrol Plug-In Hybrid': 1184, 'Petrol/Gas': 1, 'Plug-In Hybrid': 5}}, 'checkerActivity': {'deactivatedCount': 151117, 'deactivatedCountFacebook': 913, 'deactivatedCountGumtree': 13968, 'deactivatedCountAutoTrader': 53267, 'deactivatedCountMotors': 1278, 'deactivatedCountHeyCars': 2449, 'deactivatedCountHeyAiCars': 156}}
# total_active_facebook_24 =   data1["count"]["activeFacebook"]

# total_active_heycar_24   =    data1["count"]["activeHeyCars"]

# total_active_autotrader_24=   data1["count"]["activeAutoTrader"]

# total_active_gumtree_24 =     data1["count"]["activeGumtree"]

# total_active_motors_24  =      data1["count"]["activeMotors"]


# total_active_facebook_7 =   data7["count"]["activeFacebook"]

# total_active_heycar_7 =    data7["count"]["activeHeyCars"]

# total_active_autotrader_7 = data7["count"]["activeAutoTrader"]

# total_active_gumtree_7 =   data7["count"]["activeGumtree"]

# total_active_motors_7 =     data7["count"]["activeMotors"]


# total_active_facebook_15 =   data15["count"]["activeFacebook"]

# total_active_heycar_15 =    data15["count"]["activeHeyCars"]

# total_active_autotrader_15 = data15["count"]["activeAutoTrader"]

# total_active_gumtree_15 =    data15["count"]["activeGumtree"]

# total_active_motors_15 =     data15["count"]["activeMotors"]





# total_active_facebook_30 =   data30["count"]["activeFacebook"]

# total_active_heycar_30 =    data30["count"]["activeHeyCars"]

# total_active_autotrader_30 = data30["count"]["activeAutoTrader"]

# total_active_gumtree_30 =    data30["count"]["activeGumtree"]

# total_active_motors_30 =     data30["count"]["activeMotors"]




# total_active_facebook =   data_lifetime["count"]["activeFacebook"]

# total_active_heycar =    data_lifetime["count"]["activeHeyCars"]

# total_active_autotrader = data_lifetime["count"]["activeAutoTrader"]

# total_active_gumtree =    data_lifetime["count"]["activeGumtree"]

# total_active_motors =     data_lifetime["count"]["activeMotors"]


# data = {
#     'Last 24 Hours': [total_active_autotrader_24, total_active_gumtree_24, total_active_facebook_24, total_active_heycar_24, total_active_motors_24],
#     'Last 7 days': [total_active_autotrader_7, total_active_gumtree_7, total_active_facebook_7, total_active_heycar_7, total_active_motors_7],
#     'Last 15 days': [total_active_autotrader_15, total_active_gumtree_15, total_active_facebook_15, total_active_heycar_15, total_active_motors_15],
#     'Last 30 days': [total_active_autotrader_30, total_active_gumtree_30, total_active_facebook_30, total_active_heycar_30, total_active_motors_30],
#     'Lifetime': [total_active_autotrader, total_active_gumtree, total_active_facebook, total_active_heycar, total_active_motors]
# }
# df = pd.DataFrame(data, index=["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"])
# print(data_lifetime)



# var={"name":{"n2":2}}
# print(var['name'])

va="aADx-dcdcSS"
print(va.lower())