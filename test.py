import requests

def datapush():
    headers = {
        'Authorization': 'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'
    }
    APIurl = f'https://api.aicarz.com/api/v1/dev/car/65b21c848e6696cf4f53258f/deactivate'
    response = requests.request("PUT", APIurl, headers = headers)

    
    while response.status_code!=200:
        print('again hit API because response is: ',response.status_code)
        response = requests.request("PUT", APIurl, headers=headers)     
    print("Add Deactivate",response.status_code)


datapush()
