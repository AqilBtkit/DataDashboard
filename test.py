# import requests
# import json

# def dataload():
#     url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=1"
#     headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
#     response = requests.request("GET", url, headers=headers)
#     data1= json.loads(response.text)
#     print("\n\n\nStatus code::::",response.status_code)

#     # while response.status_code == 502:
#     #     response = requests.request("GET", url, headers=headers)
#     #     print("\n\n\nStatus code::::",response.status_code)
#     #     data1= json.loads(response.text)
        
#     print("Data 1 day: ",data1)
    
    
#     # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=7"
#     # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
#     # response = requests.request("GET", url, headers=headers)
#     # data7= json.loads(response.text)
#     # print("\n\n\nStatus code::::",response.status_code)

#     # # while response.status_code == 502:
#     # #     response = requests.request("GET", url, headers=headers)
#     # #     print("\n\n\nStatus code::::",response.status_code)
#     # #     data7= json.loads(response.text)
        
#     # print("Data 7 days: ",data7['data'])
    
#     # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
#     # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
#     # response = requests.request("GET", url, headers=headers)
#     # data15= json.loads(response.text)
#     # print("\n\n\nStatus code::::",response.status_code)

#     # # while response.status_code == 502:
#     # #     response = requests.request("GET", url, headers=headers)
#     # #     print("\n\n\nStatus code::::",response.status_code)
#     # #     data15= json.loads(response.text)
        
#     # print("Data 15 days: ",data15['data'])
    
#     # url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
#     # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
#     # response = requests.request("GET", url, headers=headers)
#     # data30= json.loads(response.text)
#     # print("\n\n\nStatus code::::",response.status_code)

#     # # while response.status_code == 502:
#     # #     response = requests.request("GET", url, headers=headers)
#     # #     print("\n\n\nStatus code::::",response.status_code)
#     # #     data30= json.loads(response.text)
        
#     # print("Data 30 days: ",data30['data'])
    
    
#     # url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
#     # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
#     # response = requests.request("GET", url, headers=headers)
#     # data_lifetime= json.loads(response.text)
#     # print("\n\n\nStatus code::::",response.status_code)

#     # # while response.status_code == 502:
#     # #     response = requests.request("GET", url, headers=headers)
#     # #     print("\n\n\nStatus code::::",response.status_code)
#     # #     data_lifetime= json.loads(response.text)
        
#     # print("Data lifetime: ",data_lifetime['data'])
    
#     return data1

# dataload()
# va=[23,43,54,'324',55]

# print(sum(int(va)))

car_dict = {
    'ABARTH': 1, 'ALFA ROMEO': 1, 'ASTON MARTIN': 2, 'AUDI': 121, 'AUDI Q4': 1,
    'BENTLEY': 3, 'BMW': 56, 'CHEVROLET': 3, 'CITROEN': 23, 'CUPRA': 2,
    'DACIA': 5, 'DAIHATSU': 1, 'DAIMLER': 1, 'FIAT': 8, 'FORD': 70, 'HONDA': 21,
    'HYUNDAI': 31, 'JAGUAR': 10, 'KIA': 26, 'LAMBORGHINI': 1, 'LAND ROVER': 39,
    'LEXUS': 2, 'LOTUS': 3, 'MASERATI': 2, 'MAZDA': 13, 'MERCEDES-BENZ': 58,
    'MG': 3, 'MG MOTOR UK': 3, 'MINI': 18, 'MITSUBISHI': 2, 'NISSAN': 50,
    'PEUGEOT': 42, 'POLESTAR': 1, 'PORSCHE': 15, 'RENAULT': 12, 'SEAT': 17,
    'SKODA': 28, 'SMART': 3, 'SSANGYONG': 1, 'SUBARU': 1, 'SUZUKI': 4,
    'TOYOTA': 56, 'VAUXHALL': 55, 'VOLKSWAGEN': 84, 'VOLVO': 23
}

def sort_by_value(item):
    return item[1]

sorted_cars = dict(sorted(car_dict.items(), key=sort_by_value, reverse=True))

print(sorted_cars)
