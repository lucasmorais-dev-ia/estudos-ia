import csv
import json
import sys

import httpx

# cities = cidades; cada uma com nome, latitude e longitude
cities = [
    {"name": "Cuiabá", "latitude": -15.60, "longitude": -56.10},
    {"name": "Rondonópolis", "latitude": -16.47, "longitude": -54.64},
    {"name": "Sinop", "latitude": -11.86, "longitude": -55.50},
    {"name": "Sorriso", "latitude": -12.55, "longitude": -55.71},
]

url = "https://api.open-meteo.com/v1/forecast"

results = []

for city in cities:
    params = {"latitude": city["latitude"], "longitude": city["longitude"], "current": "temperature_2m"}

    try:

        # timeout = espera no máximo 10 segundos pela resposta
        response = httpx.get(url, params=params, timeout=10)

        # raise_for_status = se a API respondeu com erro (como 404 ou 500), vira um erro do Python
        response.raise_for_status()

    except httpx.HTTPError:
        print(f"Não consegui buscar {city["name"]}")

        # continue = pula o resto desta volta e vai para a próxima cidade
        continue

    data = response.json()
    temp = data["current"]["temperature_2m"]
    results.append({"name": city["name"], "temperature": temp})

if not results:
    sys.exit("Nenhuma cidade foi buscada. Os arquivos não foram alterados.")

with open("clima.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "temperature"])
    writer.writeheader()
    for result in results:
        writer.writerow(result)

# json.dump = escrever a lista no arquivo, no formato JSON
with open("clima.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)