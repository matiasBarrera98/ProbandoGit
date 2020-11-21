import requests, json
from datetime import datetime

today = datetime.today().date()
print(today)

response = requests.get("https://mindicador.cl/api/uf")

data = json.loads(response.text)
    # Para que el json se vea ordenado, retornar pretty_json
pretty_json = json.dumps(data, indent=2)

print(f"{data['nombre']} : ${data['serie'][0]['valor']}")