import sys


def main():
    # nada depois do nome do programa
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # mais de um arquivo
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # o nome não termina em .py
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try: 
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:

        clean = line.strip()
        if clean == "":
            pass
        elif clean.startswith("#"):
            pass
        else:
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()