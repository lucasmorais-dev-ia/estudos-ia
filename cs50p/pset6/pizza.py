import csv
import sys

from tabulate import tabulate


def main():
    # nada depois do nome do programa
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # mais de um arquivo
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # o nome não termina em .csv
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try: 
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            menu = []
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    header = menu[0]
    pizzas = menu[1:]
    print(tabulate(pizzas, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()