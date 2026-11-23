import httpx
import csv

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
    response = httpx.get(url, params=params)
    data = response.json()
    temp = data["current"]["temperature_2m"]
    results.append({"name": city["name"], "temperature": temp})

with open("clima.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "temperature"])
    writer.writeheader()
    for result in results:
        writer.writerow(result)