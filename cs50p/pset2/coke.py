def main():
    # valor_devido = 50
    amount_due = 50

    # enquanto valor_devido > 0
    while amount_due > 0:
        # imprimir("Valor devido:", valor_devido)
        print("Amount Due:", amount_due)

        # moeda = inteiro(entrada("Insira a moeda: "))
        coin = int(input("Insert Coin: "))

        # se a moeda estiver em [25, 10, 5]
        if coin in [25, 10, 5]:
            # valor_devido = valor_devido - moeda
            amount_due = amount_due - coin

    # imprimir("Troco devido:", menos valor_devido)
    print("Change Owed:", -amount_due)


main()