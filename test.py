import requests
import json

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
        
    print("Data 1 day: ",data1)
    
    
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
    
    
    # url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
    # headers = {'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'}
    # response = requests.request("GET", url, headers=headers)
    # data_lifetime= json.loads(response.text)
    # print("\n\n\nStatus code::::",response.status_code)

    # # while response.status_code == 502:
    # #     response = requests.request("GET", url, headers=headers)
    # #     print("\n\n\nStatus code::::",response.status_code)
    # #     data_lifetime= json.loads(response.text)
        
    # print("Data lifetime: ",data_lifetime['data'])
    
    return data1

dataload()
# va=[23,43,54,324,55]

# print(sum(va))