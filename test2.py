# import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pymongo
from datetime import datetime, tzinfo, timezone
import requests
import json

# st.set_page_config(layout="wide")

# st.title("Data Dashboard")
# st.markdown("**________________________________________________________________________________________________________________________________________________________________________________**")
# st.header(f"Platforms")



# Sample data
# @st.cache_resource(ttl=1800)
def dataload():
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=1"
    headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    response = requests.request("GET", url, headers=headers)
    data1= json.loads(response.text)
    print("\n\n\nStatus code::::",response.status_code)

    # while response.status_code == 502:
    #     response = requests.request("GET", url, headers=headers)
    #     print("\n\n\nStatus code::::",response.status_code)
    #     data1= json.loads(response.text)
        
    print("Data 1 day: ",data1['data'])
    
    
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=7"
    headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    response = requests.request("GET", url, headers=headers)
    data7= json.loads(response.text)
    print("\n\n\nStatus code::::",response.status_code)

    # while response.status_code == 502:
    #     response = requests.request("GET", url, headers=headers)
    #     print("\n\n\nStatus code::::",response.status_code)
    #     data7= json.loads(response.text)
        
    print("Data 7 days: ",data7['data'])
    
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
    headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    response = requests.request("GET", url, headers=headers)
    data15= json.loads(response.text)
    print("\n\n\nStatus code::::",response.status_code)

    # while response.status_code == 502:
    #     response = requests.request("GET", url, headers=headers)
    #     print("\n\n\nStatus code::::",response.status_code)
    #     data15= json.loads(response.text)
        
    print("Data 15 days: ",data15['data'])
    
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
    headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    response = requests.request("GET", url, headers=headers)
    data30= json.loads(response.text)
    print("\n\n\nStatus code::::",response.status_code)

    # while response.status_code == 502:
    #     response = requests.request("GET", url, headers=headers)
    #     print("\n\n\nStatus code::::",response.status_code)
    #     data30= json.loads(response.text)
        
    print("Data 30 days: ",data30['data'])
    
    
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
    
    return data1['data'], data7['data'], data15['data'], data30['data'], data_lifetime['data']

data1, data7, data15, data30, data_lifetime= dataload()


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
print(data_lifetime)



var={"name":{"n2":2}}
print(var['name'])