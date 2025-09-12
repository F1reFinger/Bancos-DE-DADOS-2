import requests
import json

url = "https://servicodados.ibge.gov.br/api/v3/agregados"
response = requests.get(url)
print("Status:", response.status_code)
print("First 1000 chars:\n", response.text[:1000])
