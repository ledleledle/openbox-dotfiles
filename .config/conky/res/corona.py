#!/usr/bin/env python3

import requests
import json

url = "https://api.kawalcorona.com/indonesia/"

response = requests.get(url)
data = response.text
parsed = json.loads(data)

negara = parsed[0]["name"]
positif = parsed[0]['positif']
sembuh = parsed[0]['sembuh']
meninggal = parsed[0]['meninggal']

print("Data Virus Corona di negara " + negara)
print("\t+ Positif : " + positif + " jiwa")
print("\t:) Sembuh : " + sembuh + " jiwa")
print("\t:( Meninggal : " + meninggal + " jiwa")
