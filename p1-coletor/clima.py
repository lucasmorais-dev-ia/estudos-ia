import logging
import time
import csv
import json
import sys

import httpx

# basicConfig = configuração básica do registro
logging.basicConfig(
    # filename = nome do arquivo onde as mensagens são gravadas
    filename="clima.log",
    # encoding = para gravar acentos (Cuiabá) sem estragar
    encoding="utf-8",
    # level = a partir de qual importância grava (INFO grava quase tudo)
    level=logging.INFO,
    # format = como cada linha aparece: data e hora, nível e mensagem
    format="%(asctime)s %(levelname)s %(message)s",
)

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
    # repetir 3 vezes:
        # tentar buscar a cidade
        # se deu certo: sai da repetição (break)
        # se deu erro: Espera alguns segundos e tenta de novo
    # se nenhuma tentativa deu certo: "Não consegui buscar Cuiabá" depois ele pula para a proxima cidade(continue)
    
            # attempt = tentativa
    for attempt in range(3):
        try:
            response = httpx.get(url, params=params, timeout=10)
            response.raise_for_status()
            break
        except httpx.HTTPError:
            if attempt < 2:
                print(f"Tentativa {attempt + 1} falhou, tentando de novo...")
                logging.warning(f"Tentativa {attempt + 1} falhou para {city['name']}")
                time.sleep(3)
    else:
        print(f"Não consegui buscar {city['name']}")
        logging.error(f"Não consegui buscar {city['name']}")
        continue

    data = response.json()
    temp = data["current"]["temperature_2m"]
    results.append({"name": city["name"], "temperature": temp})
    logging.info(f"{city['name']}: {temp}")

if not results:
    logging.error("Nenhuma cidade foi buscada. Os arquivos não foram alterados.")
    sys.exit("Nenhuma cidade foi buscada. Os arquivos não foram alterados.")

with open("clima.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "temperature"])
    writer.writeheader()
    for result in results:
        writer.writerow(result)

# json.dump = escrever a lista no arquivo, no formato JSON
with open("clima.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)