def main():
    quantidade = pegar_quantidade()

    for i in range(quantidade):

        print(f"Caipinha {i + 1} saindo")

def pegar_quantidade():
    while True: 
        quantidade = int(input("quantas caipirinhas ? "))
        if quantidade > 0:
            return quantidade


main()