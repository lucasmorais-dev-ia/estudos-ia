import os
import sys

import requests


def main():
    # se a pessoa não digitou nada depois do nome do arquivo
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    # transformar o texto digitado em número com vírgula
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
        
    # buscar a chave guardada no Windows (nunca escrever a chave aqui)
    api_key = os.getenv("COINCAP_API_KEY")

    # pedir os dados do bitcoin para a CoinCap
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key)

    result = response.json()

    # pegar o preço de 1 bitcoin (vem como texto, precisa virar número)
    price = float(result["data"]["priceUsd"])

    # preço de 1 bitcoin vezes a quantidade que a pessoa digitou
    total = price * amount

    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()