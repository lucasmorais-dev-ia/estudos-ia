def main():


    Cardápio_e_precos = {
    "Caipirinha": 25, 
    "Mojito": 30, 
    "Gin Tropical": 35, 
    "Negroni": 40
}
    print("cardápio e precos: ")
    for drink in Cardápio_e_precos:
        print(f"{drink} custa R$ {Cardápio_e_precos[drink]}")

    pedido = input("Qual drink? ").title()
    print(f"{pedido} custa R$ {Cardápio_e_precos[pedido]}")


main()